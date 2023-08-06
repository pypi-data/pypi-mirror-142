"""
Copyright  [2021]  signal4gmns Contributors (https://github.com/asu-trans-ai-lab/Signal4GMNS)
Current Top Contributors: Xuesong (Simon) Zhou, Milan Zlatkovic, Han (Harry) Zheng

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
 """

from .yamlHandler import YamlHandler
from .Enums import *
import os
import pandas as pd
import numpy as np
import math
import datetime
from .intermediateFiles import *
from .coder import *


mesonetPath=""
micronetPath=""
movementFileName=""
macroLinkFileName=""
macroNodeFileName=""

mesoLinkFileName=""
mesoNodeFileName=""

microLinkFileName=""
microLinkBackupFileName=""
microNodeFileName=""
def set_map_folder(root):
    global mesonetPath,micronetPath,movementFileName,macroLinkFileName,macroNodeFileName,mesoLinkFileName,mesoNodeFileName
    global microLinkFileName,microNodeFileName,microLinkBackupFileName
    mesonetPath = os.path.join(root, "mesonet")
    micronetPath = os.path.join(root, "micronet")
    movementFileName = os.path.join(root, "movement.csv")
    macroLinkFileName = os.path.join(root, "link.csv")
    macroNodeFileName = os.path.join(root, "node.csv")

    mesoLinkFileName = os.path.join(mesonetPath, "link.csv")
    mesoNodeFileName = os.path.join(mesonetPath, "node.csv")

    microLinkFileName = os.path.join(micronetPath, "link.csv")
    microLinkBackupFileName = os.path.join(micronetPath, "link_backup.csv")
    microNodeFileName = os.path.join(micronetPath, "node.csv")



g_node_vector = []
g_link_vector = []
g_node_map = {}
g_link_map={}
g_inter=0

# array size, for constructing matirx or array
laneColumnSize = 32
movementSize = 12
directionSize = 4
NEMA_PhaseSize = 32  # temp enable=false
stageSize = 4
ringSize = 3
groupSize = 5
saturated_flow_rate=1900




class CMainModual:
    def __init__(self):
        self.g_number_of_links = 0
        self.g_number_of_nodes = 0
        self.b_debug_detail_flag = 1
        self.g_pFileDebugLog = None
        self.g_informationCount = 0
        self.g_internal_node_to_seq_no_map = {}
        self.g_road_link_id_map = {}
        self.g_number_of_zones = 0
        self.g_LoadingStartTimeInMin = 0
        self.g_LoadingEndTimeInMin = 0
        self.g_number_of_movements=0


class CMovementData:
    def __init__(self):
        self.Enable = False
        self.movementIndex=None
        self.LinkSeqNo = None
        self.ib_link_id=None
        self.ob_link_id=None
        self.ib_osm_node_id=None
        self.ob_osm_node_id=None
        self.StageNo_in_Order = []#enum
        self.Volume = 0
        self.Lanes = None
        self.SharedLanes = None
        self.GroupNo = None#enum
        self.DirectionNo = None#enum
        self.Left_Turn_Treatment = None
        self.Geometry=None
        self.mvmt_id=None
        self.NEMA_Phase=None
        self.Ring=None
        self.Barrier=None
        self.init_parameters_Dict=None
        self.movementCode=None
        self.node_id=None # movement.csv->intermediate files->signal_timing_phase.csv
        self.osm_node_id=None # movement.csv->intermediate files->signal_timing_phase.csv


class CSignalNode:
    def __init__(self, nodeID, xcoord, ycoord,_config_Parameters,reference_cycle_length):

        self.nodeID=nodeID
        self.xcoord=xcoord
        self.ycoord=ycoord
        self.major_Approach=E_Major_Approach.nu


        self.y_StageMax = _config_Parameters["y_StageMax"]
        self.x_c_output = _config_Parameters["x_c_output"]
        self.cycle_length = reference_cycle_length
        self.reference_cycle_length = reference_cycle_length
        self.cycle_length_min=_config_Parameters["default_c_Min"]
        self.l_value = _config_Parameters["l_value"]
        self.x_c_Input = _config_Parameters["x_c_Input"]
        self.PHF = _config_Parameters["PHF"]
        self.f_lu = _config_Parameters["f_lu"]
        self.f_hv = _config_Parameters["f_hv"]
        self.t_L = _config_Parameters["t_L"]
        self.t_Yellow = _config_Parameters["t_Yellow"]
        self.t_AR = _config_Parameters["t_AR"]
        self.minGreenTime = _config_Parameters["minGreenTime"]
        self.OSM_Node_ID=None
        self.start_time_in_min=_config_Parameters["start_time_in_min"]
        self.end_time_in_min=_config_Parameters["end_time_in_min"]
        self.use_reference_cycle_length=_config_Parameters["use_reference_cycle_length"]

        # [None] * (stageSize + 1)
        self.green_Start_Stage_Array = [0] * (stageSize + 1)
        self.green_End_Stage_Array = [0] * (stageSize + 1)
        self.y_Max_Stage_Array = [0] * (stageSize + 1)
        self.green_Time_Stage_Array = [0] * (stageSize + 1)
        self.cumulative_Green_Start_Time_Stage_Array = [0] * (stageSize + 1)
        self.cumulative_Green_End_Time_Stage_Array = [0] * (stageSize + 1)
        self.effective_Green_Time_Stage_Array = [0] * (stageSize + 1)
        self.cumulative_Effective_Green_Start_Time_Stage_Array = [0] * (stageSize + 1)
        self.cumulative_Effective_Green_End_Time_Stage_Array = [0] * (stageSize + 1)
        self.ratio_of_Effective_Green_Time_to_Cycle_Length_Array = [0] * (stageSize + 1)
        self.approach_Average_Delay_Array = [0] * (directionSize + 1)
        self.approach_Total_Delay_Array = [0] * (directionSize + 1)
        self.approach_Total_Volume_Array = [0] * (directionSize + 1)

        self.saturation_Flow_Rate_Matrix = np.empty([stageSize + 1, movementSize + 1])
        self.stage_Direction_Candidates_Matrix = np.empty([stageSize + 1, directionSize + 1, groupSize + 1])
        self.y_Stage_Movement_Matrix = np.empty([stageSize + 1, movementSize + 1])
        self.capacity_by_Stage_and_Movement_Matrix = np.empty([stageSize + 1, movementSize + 1])
        self.v_over_C_by_Stage_and_Movement_Matrix = np.empty([stageSize + 1, movementSize + 1])
        self.average_Uniform_Delay_Matrix = np.empty([stageSize + 1, movementSize + 1])
        # self.NEMA_Phase_Matrix = [[0, 0, 0, 0, 1], [5, 0, 2, 6, 0], [3, 7, 0, 4, 8]]
        # self.green_Start_NEMA_Phase = np.empty([5, 3])
        self.Stage_Ring_Movement_Matrix = {}
        for a in range(ringSize + 1):
            for b in range(stageSize + 1):
                self.Stage_Ring_Movement_Matrix[ringSize + 1, stageSize + 1] = CMovementData()

        self.movement_str_to_index_map = {}
        self.movement_str_to_index_map["EBL"] = EMovement_Index.EBL
        self.movement_str_to_index_map["EBT"] = EMovement_Index.EBT
        self.movement_str_to_index_map["EBR"] = EMovement_Index.EBR

        self.movement_str_to_index_map["WBL"] = EMovement_Index.WBL
        self.movement_str_to_index_map["WBT"] = EMovement_Index.WBT
        self.movement_str_to_index_map["WBR"] = EMovement_Index.WBR

        self.movement_str_to_index_map["NBL"] = EMovement_Index.NBL
        self.movement_str_to_index_map["NBT"] = EMovement_Index.NBT
        self.movement_str_to_index_map["NBR"] = EMovement_Index.NBR

        self.movement_str_to_index_map["SBL"] = EMovement_Index.SBL
        self.movement_str_to_index_map["SBT"] = EMovement_Index.SBT
        self.movement_str_to_index_map["SBR"] = EMovement_Index.SBR

        self.movement_str_array = {}
        self.movement_str_array[EMovement_Index.EBL] = "EBL"
        self.movement_str_array[EMovement_Index.EBT] = "EBT"
        self.movement_str_array[EMovement_Index.EBR] = "EBR"
        self.movement_str_array[EMovement_Index.WBL] = "WBL"
        self.movement_str_array[EMovement_Index.WBT] = "WBT"
        self.movement_str_array[EMovement_Index.WBR] = "WBR"
        self.movement_str_array[EMovement_Index.NBL] = "NBL"
        self.movement_str_array[EMovement_Index.NBT] = "NBT"
        self.movement_str_array[EMovement_Index.NBR] = "NBR"
        self.movement_str_array[EMovement_Index.SBL] = "SBL"
        self.movement_str_array[EMovement_Index.SBT] = "SBT"
        self.movement_str_array[EMovement_Index.SBR] = "SBR"

        self.movement_str_to_direction_map = {}
        self.movement_str_to_direction_map["EBL"] = EDirection.E
        self.movement_str_to_direction_map["EBT"] = EDirection.E
        self.movement_str_to_direction_map["EBR"] = EDirection.E

        self.movement_str_to_direction_map["WBL"] = EDirection.W
        self.movement_str_to_direction_map["WBT"] = EDirection.W
        self.movement_str_to_direction_map["WBR"] = EDirection.W

        self.movement_str_to_direction_map["NBL"] = EDirection.N
        self.movement_str_to_direction_map["NBT"] = EDirection.N
        self.movement_str_to_direction_map["NBR"] = EDirection.N

        self.movement_str_to_direction_map["SBL"] = EDirection.S
        self.movement_str_to_direction_map["SBT"] = EDirection.S
        self.movement_str_to_direction_map["SBR"] = EDirection.S

        self.left_Movement_Opposing_Index_Map = {}
        self.left_Movement_Opposing_Index_Map[EMovement_Index.EBL] = EMovement_Index.WBT
        self.left_Movement_Opposing_Index_Map[EMovement_Index.WBL] = EMovement_Index.EBT
        self.left_Movement_Opposing_Index_Map[EMovement_Index.NBL] = EMovement_Index.SBT
        self.left_Movement_Opposing_Index_Map[EMovement_Index.SBL] = EMovement_Index.NBT

        self.left_Movement_Counterpart_Index_Map = {}
        self.left_Movement_Counterpart_Index_Map[EMovement_Index.EBL] = EMovement_Index.EBT
        self.left_Movement_Counterpart_Index_Map[EMovement_Index.WBL] = EMovement_Index.WBT
        self.left_Movement_Counterpart_Index_Map[EMovement_Index.NBL] = EMovement_Index.NBT
        self.left_Movement_Counterpart_Index_Map[EMovement_Index.SBL] = EMovement_Index.SBT

        self.left_Movement_Counterpart_Right_Trun_Index_Map = {}
        self.left_Movement_Counterpart_Right_Trun_Index_Map[EMovement_Index.EBL] = EMovement_Index.EBR
        self.left_Movement_Counterpart_Right_Trun_Index_Map[EMovement_Index.WBL] = EMovement_Index.WBR
        self.left_Movement_Counterpart_Right_Trun_Index_Map[EMovement_Index.NBL] = EMovement_Index.NBR
        self.left_Movement_Counterpart_Right_Trun_Index_Map[EMovement_Index.SBL] = EMovement_Index.SBR

        self.movement_Index_to_Group_Map = {}
        self.movement_Index_to_Group_Map[EMovement_Index.EBL] = EGroup(1)
        self.movement_Index_to_Group_Map[EMovement_Index.EBT] = EGroup(2)
        self.movement_Index_to_Group_Map[EMovement_Index.EBR] = EGroup(2)
        self.movement_Index_to_Group_Map[EMovement_Index.WBL] = EGroup(1)
        self.movement_Index_to_Group_Map[EMovement_Index.WBT] = EGroup(2)
        self.movement_Index_to_Group_Map[EMovement_Index.WBR] = EGroup(2)
        self.movement_Index_to_Group_Map[EMovement_Index.NBL] = EGroup(1)
        self.movement_Index_to_Group_Map[EMovement_Index.NBT] = EGroup(2)
        self.movement_Index_to_Group_Map[EMovement_Index.NBR] = EGroup(2)
        self.movement_Index_to_Group_Map[EMovement_Index.SBL] = EGroup(1)
        self.movement_Index_to_Group_Map[EMovement_Index.SBT] = EGroup(2)
        self.movement_Index_to_Group_Map[EMovement_Index.SBR] = EGroup(2)

        self.direction_index_to_str_map = {}
        self.direction_index_to_str_map[EDirection.E] = "E"
        self.direction_index_to_str_map[EDirection.W] = "W"
        self.direction_index_to_str_map[EDirection.N] = "N"
        self.direction_index_to_str_map[EDirection.S] = "S"

        self.intersection_Average_Delay = 0
        self.intersection_Total_Delay = 0
        self.intersection_Total_Volume = 0

        self.left_Turn_Treatment_index_to_str_map = {}
        self.left_Turn_Treatment_index_to_str_map[ELeft_Turn_Treatment.prot] = "protected"
        self.left_Turn_Treatment_index_to_str_map[ELeft_Turn_Treatment.perm] = "permissive"
        self.left_Turn_Treatment_index_to_str_map[ELeft_Turn_Treatment.no_Treatment] = ""

        for s in range(stageSize + 1):
            self.y_Max_Stage_Array[s] = 0

            for m in range(movementSize + 1):
                self.saturation_Flow_Rate_Matrix[s][m] = 0
                self.capacity_by_Stage_and_Movement_Matrix[s][m] = 0

            for d in range(directionSize + 1):
                for g in range(groupSize + 1):
                    self.stage_Direction_Candidates_Matrix[s][d][g] = 0
                self.approach_Average_Delay_Array[d] = 0
                self.approach_Total_Delay_Array[d] = 0
                self.approach_Total_Volume_Array[d] = 0

        self.movement_Array = []
        self.NEMA_Frame =None
        for m in range(movementSize + 1):
            self.movement_Array.append(CMovementData())

    def Initialization(self):
        #Set Left Turn Treatment
        self.Set_Left_Turn_Treatment()
        #Set Stage No. for Movements
        self.Set_NEMA_Phase_Stage_No_for_Movements()


    def timing_process(self):
        #Set Saturation Flow Rate Matrix
        self.Set_Saturation_Flow_Rate_Matrix()
        #Calculate Max Flow Ratio
        self.Calculate_Flow_of_Ratio_Max()
        #Calculate Total Cycle Lost Time
        self.Calculate_Total_Cycle_Lost_Time()
        #Calculate the Minimum and Optimal Cycle Length
        self.Calculate_the_Minimum_And_Optimal_Cycle_Length()
        #Calculate x_c"
        self.Calculate_the_x_c_Output()
        #Calculate Green Time for Stages
        self.Calculate_Green_Time_for_Stages()
        #Print Green Time for Stages
        self.Printing_Green_Time_for_Stages()
        #Calculate Capacity and V over C Ratio
        self.Calculate_Capacity_And_Ratio_V_over_C()
        #Calculate Signal Delay
        self.Calculate_Signal_Delay(self.nodeID)
        #Determine Signal Intersection LOS
        self.Determine_Signal_Intersection_LOS(self.nodeID)
    def AddMovementVolume_Additional (self,str_movement, StageNo_in_Order, GroupNo, DirectionNo,movementCode):
        mi = self.movement_str_to_index_map[str_movement]
        index=int(mi.value)
        self.movement_Array[index].StageNo_in_Order = StageNo_in_Order
        self.movement_Array[index].GroupNo = GroupNo
        self.movement_Array[index].DirectionNo = DirectionNo
        self.movement_Array[index].movementCode=movementCode


    def AddMovementVolume (self, osm_node_id, node_id, ib_link_id, ob_link_id, ib_osm_node_id, ob_osm_node_id, str_movement, volume, lanes, sharedLanes, geometry, mvmt_id):
        mi = self.movement_str_to_index_map[str_movement]
        index=int(mi.value)
        di = EDirection(self.movement_str_to_direction_map[str_movement])
        self.movement_Array[index].Enable = True
        self.movement_Array[index].movementIndex=mi
        self.movement_Array[index].osm_node_id=osm_node_id
        self.movement_Array[index].node_id=node_id
        self.movement_Array[index].ib_link_id = ib_link_id
        self.movement_Array[index].ob_link_id = ob_link_id
        self.movement_Array[index].ib_osm_node_id = ib_osm_node_id
        self.movement_Array[index].ob_osm_node_id = ob_osm_node_id
        self.movement_Array[index].Volume = volume
        self.movement_Array[index].NEMA_Phase=E_NEMA_Phase.nu
        self.movement_Array[index].Ring=E_NEMA_Ring.nu
        self.movement_Array[index].Barrier=E_NEMA_Barrier.nu
        self.movement_Array[index].GroupNo = self.movement_Index_to_Group_Map[mi]
        self.movement_Array[index].DirectionNo = di
        self.movement_Array[index].Left_Turn_Treatment = ELeft_Turn_Treatment.no_Treatment
        self.movement_Array[index].Lanes = lanes
        self.movement_Array[index].SharedLanes = sharedLanes
        self.movement_Array[index].Geometry=geometry
        self.movement_Array[index].mvmt_id=mvmt_id

    def Set_Left_Turn_Treatment(self):
        for m in range(1, movementSize + 1):
            if not self.movement_Array[m].Enable:
                continue
            if self.movement_Array[m].GroupNo.value == 1:
                final_decision = 0
                # (1)Left-turn Lane Check
                if self.movement_Array[m].Lanes > 1:
                    final_decision = 1
                # (2)Minimum Volume Check
                if self.movement_Array[m].Volume >= 240:
                    final_decision = 1
                # (3)Opposing Through Lanes Check
                op_Movement_Index = self.left_Movement_Opposing_Index_Map[EMovement_Index(m)]
                if (self.movement_Array[op_Movement_Index.value].Lanes != None and self.movement_Array[op_Movement_Index.value].Lanes >= 4):
                    final_decision = 1
                # (4)Opposing Traffic Speed Check

                # (5)Minimum Cross-Product Check
                co_Movement_Index = self.left_Movement_Opposing_Index_Map[EMovement_Index(m)]
                if (self.movement_Array[co_Movement_Index.value].Lanes!=None and self.movement_Array[co_Movement_Index.value].Lanes > 1):
                    if self.movement_Array[co_Movement_Index.value].Volume * self.movement_Array[m].Volume >= 100000:
                        final_decision = 1
                else:
                    if self.movement_Array[co_Movement_Index.value].Volume * self.movement_Array[m].Volume >= 50000:
                        final_decision = 1
                # (6)if there is no T movement, then the left movement should be protected"""
                if self.movement_Array[
                    self.left_Movement_Counterpart_Index_Map[EMovement_Index(m)].value].Enable == False:
                    final_decision = 1
            else:
                final_decision = -1

            self.movement_Array[m].Left_Turn_Treatment = ELeft_Turn_Treatment(final_decision)

    def Set_Major_Apporach(self):
        east_And_West_Volume = self.movement_Array[EMovement_Index.EBL.value].Volume + self.movement_Array[
            EMovement_Index.EBT.value].Volume + self.movement_Array[EMovement_Index.EBR.value].Volume + \
                               self.movement_Array[EMovement_Index.WBL.value].Volume + self.movement_Array[
                                   EMovement_Index.WBT.value].Volume + self.movement_Array[
                                   EMovement_Index.WBR.value].Volume
        north_And_South_Volume = self.movement_Array[EMovement_Index.NBL.value].Volume + self.movement_Array[
            EMovement_Index.NBT.value].Volume + self.movement_Array[EMovement_Index.NBR.value].Volume + \
                                 self.movement_Array[EMovement_Index.SBL.value].Volume + self.movement_Array[
                                     EMovement_Index.SBT.value].Volume + self.movement_Array[
                                     EMovement_Index.SBR.value].Volume

        if (east_And_West_Volume >= north_And_South_Volume):
            self.EW_OR_NS = True
        else:
            self.EW_OR_NS = False
        self.major_Approach = E_Major_Approach.EW if self.EW_OR_NS else E_Major_Approach.NS

    def Set_NEMA_Phase_Stage_No_for_Movements(self):
        from .NEMA_Frame import NEMA_Frame
        self.NEMA_Frame=NEMA_Frame(self)
        self.NEMA_Frame.Assign_NEMA_Phase(self.EW_OR_NS)
        ring_Phase_Dict=self.NEMA_Frame.Get_Phases_of_Rings()
        barrier_Phase_Dict=self.NEMA_Frame.Get_Phases_of_Barriers()
        stage_Movement_Dict=self.NEMA_Frame.Get_Movements_of_Stages()
        movement_Stage_Dict=self.NEMA_Frame.Get_Stage_of_Movement()
        movement_NEMA_Table=self.NEMA_Frame.Get_Movement_NEMA_Table()


        remove_Stage_List=[]
        for stage,movement_list in stage_Movement_Dict.items():
            if stage.value%2==1:
                if len(movement_list)==0:
                    remove_Stage_List.append(stage)
                    continue
                protection_count=0
                for movement in movement_list:
                    if self.movement_Array[movement.value].Left_Turn_Treatment==ELeft_Turn_Treatment.prot:
                        protection_count+=1
                    else:
                        pass
                if protection_count==0:
                    remove_Stage_List.append(stage)
        move_index=0
        for start_stage in remove_Stage_List:
            for stage_value in range(start_stage.value+1-move_index,4+1-move_index):
                for key,stage in movement_Stage_Dict.items():
                    if stage.value==stage_value:
                        movement_Stage_Dict[key]=EStage(stage.value-1)
            move_index+=1

        for movement in self.movement_Array:
            if movement.Enable==True:
                movement.StageNo_in_Order.append(movement_Stage_Dict[movement.movementIndex])
                movement.NEMA_Phase=movement_NEMA_Table[movement.movementIndex]
                for ring,NEMA_Phase in ring_Phase_Dict.items():
                    if movement.NEMA_Phase in NEMA_Phase:
                        movement.Ring=ring
                for barrier,NEMA_Phase in barrier_Phase_Dict.items():
                    if movement.NEMA_Phase in NEMA_Phase:
                        movement.Barrier=barrier

        self.stage_Actual_Size=4-len(remove_Stage_List)
        return

    def Set_Saturation_Flow_Rate_Matrix(self):
        for m in range(1, movementSize + 1):
            if self.movement_Array[m].Enable == False:
                continue
            for so in range(len(self.movement_Array[m].StageNo_in_Order)):
                if self.movement_Array[m].Left_Turn_Treatment.name == "prot":
                    self.saturation_Flow_Rate_Matrix[self.movement_Array[m].StageNo_in_Order[so].value][m] = saturated_flow_rate * self.movement_Array[m].Lanes * self.PHF
                elif self.movement_Array[m].Left_Turn_Treatment.name == "perm":
                    op_Movement_Index = self.left_Movement_Opposing_Index_Map[EMovement_Index(m)]
                    op_volume = self.movement_Array[op_Movement_Index.value].Volume
                    if self.movement_Array[op_Movement_Index.value].Enable==False:
                        self.saturation_Flow_Rate_Matrix[self.movement_Array[m].StageNo_in_Order[so].value][m] =160
                    else:
                        temp=self.f_lu * self.f_hv * op_volume * math.exp((-op_volume * 4.5 / 3600)) / (1 - math.exp(-op_volume * 2.5 / 3600))
                        if temp>0:
                            self.saturation_Flow_Rate_Matrix[self.movement_Array[m].StageNo_in_Order[so].value][m] = temp
                        else:
                            self.saturation_Flow_Rate_Matrix[self.movement_Array[m].StageNo_in_Order[so].value][m]=saturated_flow_rate *self.movement_Array[m].Lanes
                else:
                    self.saturation_Flow_Rate_Matrix[self.movement_Array[m].StageNo_in_Order[so].value][m] = saturated_flow_rate *self.movement_Array[m].Lanes


    #The sum of the flow ratios for the critical lane groups for this phasing plan will be needed for the next section.
    # Since this phasing plan does not include any overlapping phases,
    # this value is simply the sum of the highest lane group v/s ratios for the three stages, as follows:
    def Calculate_Flow_of_Ratio_Max(self):
        for s in range(1, self.stage_Actual_Size + 1):
            self.y_Max_Stage_Array[s] = 0
            for m in range(1, movementSize + 1):
                for so in range(len(self.movement_Array[m].StageNo_in_Order)):
                    if self.saturation_Flow_Rate_Matrix[s][m] != 0 and self.movement_Array[m].Enable and self.movement_Array[m].StageNo_in_Order[so].value == s:
                        self.y_Stage_Movement_Matrix[s][m] = self.movement_Array[m].Volume / self.saturation_Flow_Rate_Matrix[s][m]
                        self.stage_Direction_Candidates_Matrix[s][self.movement_Array[m].DirectionNo.value][
                            self.movement_Array[m].GroupNo.value] += self.y_Stage_Movement_Matrix[s][m]
                        if self.stage_Direction_Candidates_Matrix[s][self.movement_Array[m].DirectionNo.value][
                            self.movement_Array[m].GroupNo.value] >= self.y_Max_Stage_Array[s]:
                            self.y_Max_Stage_Array[s] = self.stage_Direction_Candidates_Matrix[s][self.movement_Array[m].DirectionNo.value][
                                self.movement_Array[m].GroupNo.value]
        self.y_StageMax = 0
        for i in range(1, self.stage_Actual_Size + 1):
            self.y_StageMax += self.y_Max_Stage_Array[i]

    def Calculate_Total_Cycle_Lost_Time(self):
        self.l_value = self.t_L * self.stage_Actual_Size

    def Calculate_the_Minimum_And_Optimal_Cycle_Length(self):
        calculated_cycle_length=(self.l_value * self.x_c_Input) / (self.x_c_Input - self.y_StageMax)
        if self.use_reference_cycle_length:
            self.cycle_length=self.reference_cycle_length
        else:
            if calculated_cycle_length > 0:
                self.cycle_length = min(self.cycle_length_min, calculated_cycle_length)
            else:
                self.cycle_length=self.cycle_length_min

        self.c_Optimal = max(60, (1.5 * self.l_value + 5) / (1 - self.y_StageMax) if self.y_StageMax != 1 else (1.5 * self.l_value + 5))

    def Calculate_the_x_c_Output(self):
        self.x_c_output = round((self.y_StageMax * self.cycle_length) / (self.cycle_length - self.l_value),3)

    def Calculate_Green_Time_for_Stages(self):
        assigned_green_time=0
        for s in range(1, self.stage_Actual_Size + 1):
            greenTime=max(self.minGreenTime, self.y_Max_Stage_Array[s] * self.cycle_length / self.y_StageMax)
            # greenTime=min(self.reference_cycle_length-15-assigned_green_time,greenTime)
            greenTime = min(self.reference_cycle_length - assigned_green_time, greenTime)
            self.green_Time_Stage_Array[s] = greenTime
            assigned_green_time+=greenTime
            self.effective_Green_Time_Stage_Array[s] = self.green_Time_Stage_Array[s] - self.t_L + self.t_Yellow + self.t_AR
            self.ratio_of_Effective_Green_Time_to_Cycle_Length_Array[s] = self.effective_Green_Time_Stage_Array[s] / self.cycle_length

    def Printing_Green_Time_for_Stages(self):
        self.cumulative_Green_Start_Time_Stage_Array[1] = 0
        self.cumulative_Green_End_Time_Stage_Array[1] = self.green_Time_Stage_Array[1]

        for i in range(2, self.stage_Actual_Size + 1):
            self.cumulative_Green_Start_Time_Stage_Array[i] = self.cumulative_Green_End_Time_Stage_Array[i - 1]
            self.cumulative_Green_End_Time_Stage_Array[i] = self.cumulative_Green_Start_Time_Stage_Array[i] + self.green_Time_Stage_Array[i]

        self.cumulative_Effective_Green_Start_Time_Stage_Array[1] = 0
        self.cumulative_Effective_Green_End_Time_Stage_Array[1] = self.effective_Green_Time_Stage_Array[1]

        for i in range(2, self.stage_Actual_Size + 1):
            self.cumulative_Effective_Green_Start_Time_Stage_Array[i] = self.cumulative_Effective_Green_End_Time_Stage_Array[i - 1]
            self.cumulative_Effective_Green_End_Time_Stage_Array[i] = self.cumulative_Effective_Green_Start_Time_Stage_Array[i] + self.effective_Green_Time_Stage_Array[i]


    def Calculate_Capacity_And_Ratio_V_over_C(self):
        for s in range(1, self.stage_Actual_Size + 1):
            for m in range(1, movementSize + 1):
                for so in range(len(self.movement_Array[m].StageNo_in_Order)):
                    if self.saturation_Flow_Rate_Matrix[s][m] != 0 and self.movement_Array[m].Enable and self.movement_Array[m].StageNo_in_Order[so].value == s:
                        self.capacity_by_Stage_and_Movement_Matrix[s][m] = self.saturation_Flow_Rate_Matrix[s][m] * self.ratio_of_Effective_Green_Time_to_Cycle_Length_Array[s]

                        self.v_over_C_by_Stage_and_Movement_Matrix[s][m] = self.movement_Array[m].Volume / self.capacity_by_Stage_and_Movement_Matrix[s][m]


    def Calculate_Signal_Delay(self, nodeID):
        for s in range(1, self.stage_Actual_Size + 1):
            for m in range(1, movementSize + 1):
                for so in range(len(self.movement_Array[m].StageNo_in_Order)):
                    if self.saturation_Flow_Rate_Matrix[s][m] != 0 and self.movement_Array[m].Enable and self.movement_Array[m].StageNo_in_Order[so].value == s:
                        self.average_Uniform_Delay_Matrix[s][m] = (0.5 * self.capacity_by_Stage_and_Movement_Matrix[s][m] * pow((1 - self.ratio_of_Effective_Green_Time_to_Cycle_Length_Array[s]), 2)) / (1 -self.v_over_C_by_Stage_and_Movement_Matrix[s][m] *self.ratio_of_Effective_Green_Time_to_Cycle_Length_Array[s])
                        self.approach_Total_Delay_Array[self.movement_Array[m].DirectionNo.value] += self.movement_Array[m].Volume * self.average_Uniform_Delay_Matrix[s][m]
                        self.approach_Total_Volume_Array[self.movement_Array[m].DirectionNo.value] += self.movement_Array[m].Volume
        for d in range(1, directionSize + 1):
            if self.approach_Total_Volume_Array[d] == 0:
                continue
            self.approach_Average_Delay_Array[d] = self.approach_Total_Delay_Array[d] / self.approach_Total_Volume_Array[d]
            self.intersection_Total_Delay += self.approach_Average_Delay_Array[d] * self.approach_Total_Volume_Array[d]
            self.intersection_Total_Volume += self.approach_Total_Volume_Array[d]
        self.intersection_Average_Delay = self.intersection_Total_Delay / self.intersection_Total_Volume


    def Determine_Signal_Intersection_LOS(self, nodeID):
        if self.intersection_Total_Delay <= 10:
            self.LOS = "A"
        elif self.intersection_Total_Delay <= 20:
            self.LOS = "B"
        elif self.intersection_Total_Delay <= 35:
            self.LOS = "C"
        elif self.intersection_Total_Delay <= 55:
            self.LOS = "D"
        elif self.intersection_Total_Delay <= 80:
            self.LOS = "E"
        else:
            self.LOS = "F"


class CNode:
    def __init__(self):
        self.node_seq_no = -1
        self.node_id = 0
        self.x = 0.0001
        self.y = 0.0001
        self.m_outgoing_link_seq_no_vector = []
        self.m_incoming_link_seq_no_vector = []
        self.m_to_node_seq_no_vector = []
        self.m_to_node_2_link_seq_no_map = {}
        self.osm_node_id=-1


class CLink:
    def __init__(self):
        self.free_flow_travel_time_in_min = 1
        self.zone_seq_no_for_outgoing_connector = 0
        self.m_RandomSeed = 0
        self.link_seq_no = 0
        self.link_id = ""
        self.from_node_seq_no = 0
        self.to_node_seq_no = 0
        self.link_type = 0
        self.fftt = 0.001
        self.free_flow_travel_time_in_min = 0.001
        self.lane_capacity = 0.001
        self.number_of_lanes = 0
        self.type = 0
        self.length = 0.001

def set_working_directory(data_Set_Path):
    os.getcwd()
    if not data_Set_Path=="":
        os.chdir(data_Set_Path)
        path=data_Set_Path
    else:
        path="root"

# Instance
mainModual = CMainModual()
data_Set_Path = r''
set_working_directory(data_Set_Path)

def Configuration():
    # curPath = os.path.dirname(os.path.realpath(__file__))
    working_directory = os.getcwd()
    #templateFullFileName = os.path.join(".signal4gmns", "config.yaml")
    #template_yaml = YamlHandler(templateFullFileName)
    template_yaml = YamlHandler("")
    yamlPath = os.path.join(working_directory, "config.yaml")
    bool_yaml_existence_flag = os.path.exists(yamlPath)

    if not bool_yaml_existence_flag:
        template_yaml_data_dic = template_yaml.get_default_config_dic()
        config_yaml = YamlHandler(yamlPath)
        config_yaml.write_yaml(template_yaml_data_dic)

    config_yaml = YamlHandler(yamlPath)
    _config_Parameters = config_yaml.get_ymal_data()
    return  _config_Parameters

def load_movement_data_and_volume():
    mainModual.g_number_of_nodes = 0
    mainModual.g_number_of_links = 0
    mainModual.g_number_of_movements=0
    internal_node_seq_no = 0
    _config_Parameters=Configuration()

    parser_movement = pd.read_csv(movementFileName)#"movement.csv"
    parser = pd.read_csv(macroNodeFileName,converters = {"osm_node_id":str})#"node.csv"

    pass_node_list=[]

    for i in range(len(parser_movement["mvmt_id"])):
        movementStr = str(parser_movement["mvmt_txt_id"][i])#movement_str
        if "U" in movementStr:
            continue
        mvmt_id=str(parser_movement["mvmt_id"][i])
        osm_node_id= str(parser_movement["osm_node_id"][i])
        node_id = str(parser_movement["node_id"][i])
        if "geometry" in list(parser_movement.columns.values):
            geometry=parser_movement["geometry"][i]
        else:
            geometry=""
        ib_link_id=parser_movement["ib_link_id"][i]
        ob_link_id = parser_movement["ob_link_id"][i]
        ib_osm_node_id=parser_movement["ib_osm_node_id"][i] # for timing.csv
        ob_osm_node_id=parser_movement["ob_osm_node_id"][i] #for timing.csv
        main_node_id = str(parser_movement["osm_node_id"][i])
        lanes = parser_movement["lanes"][i]
        init_volume =parser_movement["volume"][i]
        if(math.isnan(init_volume) and _config_Parameters["default_volume_filled_by_code"]):
            if "L" in movementStr:
                init_volume=105* lanes
            elif "R"in movementStr:
                init_volume=110*lanes
            else:
                init_volume=310*lanes
        # sharedLanes = parser_movement["sharedLanes"][i]
        sharedLanes = 1
        if main_node_id in pass_node_list:
            continue
        if len(movementStr) > 0 and movementStr != "nan":
            if main_node_id !="nan":
                if main_node_id not in g_node_map.keys():
                    row=parser[parser["osm_node_id"]==main_node_id]
                    ctrl_type=row["ctrl_type"].values[0]
                    if ctrl_type!="signal" and ctrl_type!="1":
                        pass_node_list.append(main_node_id)
                        continue
                    xcoord=row["x_coord"].values[0]
                    ycoord = row["y_coord"].values[0]
                    rcl=str(row["reference_cycle_length"].values[0])
                    reference_cycle_length = int(float(rcl)) if rcl !="nan" else 0
                    mainModual.g_internal_node_to_seq_no_map[main_node_id] = internal_node_seq_no
                    internal_node_seq_no+=1
                    mainModual.g_number_of_nodes += 1
                    g_node_map[main_node_id] = CSignalNode(main_node_id,
                                                           xcoord,
                                                           ycoord,
                                                           _config_Parameters,
                                                           reference_cycle_length)
                g_node_map[main_node_id].AddMovementVolume(osm_node_id,
                                                           node_id,
                                                           ib_link_id,
                                                           ob_link_id,
                                                           ib_osm_node_id,
                                                           ob_osm_node_id,
                                                           movementStr,
                                                           init_volume,
                                                           lanes,
                                                           sharedLanes,
                                                           geometry,
                                                           mvmt_id)
                g_node_map[main_node_id].OSM_Node_ID=main_node_id
                mainModual.g_number_of_movements +=1
    g_info_String = "Number of Nodes = "
    g_info_String += str(mainModual.g_number_of_nodes)

    g_info_String = "Number of Movement = "
    g_info_String += str(mainModual.g_number_of_movements)





def Get_Signal_Timing_Movement_Info():
    signal_timing_phase_list = []
    signal_phase_mvmt_list = []
    for node_id, sn in g_node_map.items():
        max_green_time = max(sn.green_Time_Stage_Array)
        cycle_length_in_sec = int(max(10, sn.cycle_length, max_green_time))
        cycle_num = int((sn.end_time_in_min - sn.start_time_in_min) * 60 / cycle_length_in_sec)
        offset_in_sec = 0
        start_time_in_sec = int(sn.start_time_in_min * 60 + offset_in_sec)
        signal_phase_mvmt_id = 0

        for m in range(1, movementSize + 1):
            if sn.movement_Array[m].Enable:
                for so in range(len(sn.movement_Array[m].StageNo_in_Order)):
                    StageNo = sn.movement_Array[m].StageNo_in_Order[so]
                    cy=0
                    start=0
                    start_green_time_in_sec =int(sn.cumulative_Green_Start_Time_Stage_Array[
                                                   StageNo.value] + cycle_length_in_sec * cy + start*start_time_in_sec)
                    end_green_time_in_sec = min(cycle_length_in_sec,int(sn.cumulative_Green_End_Time_Stage_Array[
                                                 StageNo.value] + cycle_length_in_sec * cy + start*start_time_in_sec))
                    start_hour = int(start_green_time_in_sec / 3600)
                    start_min = int(start_green_time_in_sec / 60 - start_hour * 60)
                    start_sec = int(start_green_time_in_sec % 60)
                    end_hour = int(end_green_time_in_sec / 3600)
                    end_min = int(end_green_time_in_sec / 60 - end_hour * 60)
                    end_sec = int(end_green_time_in_sec % 60)
                    green_time_window= str(start_hour).rjust(2, "0") + str(start_min).rjust(2, "0") + str(start_sec).rjust(2, "0") + "_" + str(
                            end_hour).rjust(2, "0") + str(end_min).rjust(2, "0") + str(end_sec).rjust(2, "0")

                    # from_node_id = g_node_vector[g_link_vector[sn.movement_Array[m].ib_link_id].from_node_seq_no].node_id
                    # to_node_id = g_node_vector[g_link_vector[sn.movement_Array[m].ob_link_id].to_node_seq_no].node_id
                    # capacity = int(sn.green_Time_Stage_Array[StageNo.value] * 1800.0 / 3600.0)
                    capacity = abs(sn.capacity_by_Stage_and_Movement_Matrix[StageNo.value][m])
                    v_over_c = abs(sn.v_over_C_by_Stage_and_Movement_Matrix[StageNo.value][m])
                    # greenTime = int(sn.green_Time_Stage_Array[StageNo.value])
                    greenTime=end_green_time_in_sec- start_green_time_in_sec
                    osm_web_address=f"http://openstreetmap.org/node/{node_id}"
                    #redTime = int(cycle_length_in_sec - greenTime)
                    redTime = int(cycle_length_in_sec - end_green_time_in_sec)
                    NEMA_Phase=sn.movement_Array[m].NEMA_Phase
                    ring=sn.movement_Array[m].Ring

                    barrier=sn.movement_Array[m].Barrier
                    signal_timing_phase_list.append([
                        sn.movement_Array[m].mvmt_id,  # mvmt_id
                        StageNo.value,  # timing_phase_id
                        # EMovement_Index(m).name,  # movement str
                        0,  # time_plan_id
                        green_time_window,#time_window
                        f"{NEMA_Phase.value}",  # signal_phase_num
                        greenTime,  # min_green
                        greenTime,  # max_green
                        start_green_time_in_sec,  #Start Green Time
                        end_green_time_in_sec,#End Green Time
                        "",  # extension
                        "",  # clearance
                        redTime,  # walk_time
                        cycle_length_in_sec,#cycle_length_in_sec
                        "",  # ped_clearance
                        sn.movement_Array[m].movementIndex.name,#mvmt_txt_id movement_str
                        f"{ring.value}",  # ring
                        f"{barrier.value}",  # barrier
                        StageNo.value, #stageNO
                        "",  # position
                        capacity,
                        v_over_c,
                        osm_web_address,#osm_web_address
                        sn.movement_Array[m].Geometry  # geometry
                    ])
                    protection=sn.left_Turn_Treatment_index_to_str_map[sn.movement_Array[m].Left_Turn_Treatment]
                    if protection=="":
                        protection="protected"
                    signal_phase_mvmt_list.append([
                        signal_phase_mvmt_id,  # signal_phase_mvmt_id
                        "",  # controller_id
                        # StageNo.value,  # timing_phase_id
                        sn.movement_Array[m].movementIndex.name,#mvmt_txt_id
                        f"{NEMA_Phase.value}",  # signal_phase_num
                        StageNo.value,  # stage_no
                        0,  # timing_plan_id
                        sn.movement_Array[m].mvmt_id,  # mvmt_id
                        sn.movement_Array[m].node_id,
                        sn.movement_Array[m].osm_node_id,
                        sn.movement_Array[m].ib_link_id,  # ib_link_id
                        sn.movement_Array[m].ob_link_id,  # ib_link_id
                        sn.movement_Array[m].ib_osm_node_id,  # ib_osm_node_id
                        sn.movement_Array[m].ob_osm_node_id,  # ob_osm_node_id
                        protection,  # protection
                        osm_web_address,#osm_web_address
                        sn.movement_Array[m].Geometry  # geometry
                    ])
                    signal_phase_mvmt_id += 1
    return signal_timing_phase_list, signal_phase_mvmt_list

def output_signal_phasing_files():
    signal_timing_phase_list, signal_phase_mvmt_list=Get_Signal_Timing_Movement_Info()

    signal_timing_phase_list_df=pd.DataFrame(signal_timing_phase_list,
                                             columns=["mvmt_id",
                                                      "timing_phase_id",
                                                      "timing_plan_id",
                                                      "green_time_window",
                                                      "signal_phase_num",
                                                      "min_green",
                                                      "max_green",
                                                      "start_green_time",#"green_start_time"
                                                      "end_green_time", #"green_end_time"
                                                      "extension",
                                                      "clearance",
                                                      "walk_time",
                                                      "cycle_length",
                                                      "ped_clearance",
                                                      "mvmt_txt_id",
                                                      "ring",
                                                      "barrier",
                                                      "stage_no",
                                                      "position",
                                                      "capacity",
                                                      "v_over_c",
                                                      "osm_web_address",
                                                      "geometry"])
    signal_phase_mvmt_list_df=pd.DataFrame(signal_phase_mvmt_list,
                                             columns=["signal_phase_mvmt_id",
                                                      "controller_id",
                                                      "mvmt_txt_id",
                                                      "signal_phase_num",
                                                      "stage_no",
                                                      "timing_plan_id",
                                                      "mvmt_id",
                                                      "node_id",
                                                      "osm_node_id",
                                                      "ib_link_id",
                                                      "ob_link_id",
                                                      "ib_osm_node_id",
                                                      "ob_osm_node_id",
                                                      "protection",
                                                      "osm_web_address",
                                                      "geometry"])#"timing_phase_id",

    signal_timing_phase_list_df.to_csv("signal_timing_phase.csv",index=False)
    signal_phase_mvmt_list_df.to_csv("signal_phase_mvmt.csv",index=False)


def Read_Signal_Timing_Phase_Movement_Files_Data():
    parser_signal_timing_phase = pd.read_csv(f"signal_timing_phase.csv")
    parser_signal_phase_mvmt = pd.read_csv(f"signal_phase_mvmt.csv")
    merge_table=pd.merge(parser_signal_timing_phase,parser_signal_phase_mvmt,on="mvmt_id")
    return merge_table
def Get_Timing_Info(merge_table):
    timing_file_list = []

    for i in range(len(merge_table["mvmt_id"])):
        mvmt_id = str(merge_table["mvmt_id"][i])
        osm_node_id = str(merge_table["osm_node_id"][i])
        node_id=str(merge_table["node_id"][i])
        ib_link_id=str(merge_table["ib_link_id"][i])
        ob_link_id=str(merge_table["ob_link_id"][i])
        ib_osm_node_id=str(merge_table["ib_osm_node_id"][i])
        ob_osm_node_id=str(merge_table["ob_osm_node_id"][i])
        signal_phase_num=str(merge_table["signal_phase_num_x"][i])
        ring=str(merge_table["ring"][i])
        barrier=str(merge_table["barrier"][i])
        stage_no=str(merge_table["stage_no_x"][i])
        timing_plan_id=str(merge_table["timing_plan_id_x"][i])
        green_time_window=str(merge_table["green_time_window"][i])
        green_time=str(merge_table["min_green"][i])
        cycle_length_in_sec=str(merge_table["cycle_length"][i])
        start_green_time=str(merge_table["start_green_time"][i])#"green_start_time"
        end_green_time=str(merge_table["end_green_time"][i])#"green_end_time"
        walk_time=str(merge_table["walk_time"][i])
        osm_web_address=str(merge_table["osm_web_address_x"][i])
        capacity=str(merge_table["capacity"][i])
        v_over_c=str(merge_table["v_over_c"][i])
        mvmt_txt_id=str(merge_table["mvmt_txt_id_x"][i])#mvmt_txt_id movement_str
        protection=str(merge_table["protection"][i])
        if protection=="nan":
            protection=""
        geometry=str(merge_table["geometry_x"][i])

        timing_file_list.append([
            mvmt_id,
            osm_node_id,
            node_id,
            ib_link_id,
            ob_link_id,
            ib_osm_node_id,
            ob_osm_node_id,
            signal_phase_num,
            ring,
            barrier,
            stage_no,
            timing_plan_id,
            green_time_window,
            green_time,
            cycle_length_in_sec,
            start_green_time,
            end_green_time,
            walk_time,
            capacity,
            v_over_c,
            mvmt_txt_id,#mvmt_txt_id
            protection,
            osm_web_address,
            geometry
        ])
    return timing_file_list
def output_signal_timing_file_and_modify_microLink_file():
    merge_table=Read_Signal_Timing_Phase_Movement_Files_Data()
    timing_file_list=Get_Timing_Info(merge_table)
    timing_file_list_df = pd.DataFrame(timing_file_list,
                                             columns=[  "mvmt_id",
                                                        "osm_node_id",
                                                        "node_id",
                                                        "ib_link_id",
                                                        "ob_link_id",
                                                        "ib_osm_node_id",
                                                        "ob_osm_node_id",
                                                        "signal_phase_num",
                                                        "ring",
                                                        "barrier",
                                                        "stage_no",
                                                        "timing_plan_id",
                                                        "green_time_window",
                                                        "green_time",
                                                        "cycle_length",
                                                        "start_green_time", #"green_start_time"
                                                        "end_green_time",#"green_end_time"
                                                        "red_time",
                                                        "capacity",
                                                        "v_over_c",
                                                        "mvmt_txt_id",
                                                        "protection",
                                                        "osm_web_address",
                                                        "geometry"
                                                      ])
    timing_file_list_df.to_csv("timing.csv", index=False)

    if not os.path.exists(microLinkBackupFileName):
        microLinkDataFrame = pd.read_csv(microLinkFileName, dtype="str")
        microLinkDataFrame.to_csv(microLinkBackupFileName, index=False)


    microLinkDataFrame = pd.read_csv(microLinkBackupFileName, dtype="str")


    part_timing_file_list_df=pd.DataFrame(timing_file_list_df,columns=["node_id","mvmt_txt_id","cycle_length","stage_no","green_time","red_time","start_green_time","end_green_time","capacity"])
    part_timing_file_list_df.rename(columns={"node_id":"macro_node_id"},inplace=True)
    part_timing_file_list_df.rename(columns={"capacity": "updated_capacity"}, inplace=True)
    updatedMicroLink=pd.merge(microLinkDataFrame,part_timing_file_list_df,on=["macro_node_id","mvmt_txt_id"],how="left")


    updatedMicroLink.to_csv(microLinkFileName, index=False)



    print("Finished."
          " Thanks for using signal4gmns."
                  " Please use your favorite social media platform to spread the word: https://pypi.org/project/signal4gmns/."
                  " Please report issues and suggestions at https://github.com/asu-trans-ai-lab/signal4gmns. Thanks！", 0)




def Output_Intermediate_Files(label_name="setting"):
    #output signal_Node and signal_Movement
    signal_Node_List=CSignal_Node_Interm_List()
    signal_Movement_List=CSignal_Movement_Interm_List()
    for osmID,signal_Node in g_node_map.items():
        approach_Existed_Movement_Matrix={"L":[1,1,1,1],"T":[1,1,1,1],"R":[1,1,1,1]}
        for m in range (1,movementSize+1):
            if m%3==1:
                if signal_Node.movement_Array[m].Enable==False:
                    approach_Existed_Movement_Matrix["L"][(m-1)//3]=0
            elif m%3==2:
                if signal_Node.movement_Array[m].Enable==False:
                    approach_Existed_Movement_Matrix["T"][(m-1)//3]=0
            else:
                if signal_Node.movement_Array[m].Enable==False:
                    approach_Existed_Movement_Matrix["R"][(m-1)//3]=0

        signal_Node_Code=GetSignalCode(signal_Node.major_Approach,approach_Existed_Movement_Matrix,str(osmID))
        if signal_Node.reference_cycle_length==0:
            signal_Node.reference_cycle_length=120 if "#" in signal_Node_Code else 90
        new_Output_Node=CSignal_Node_Inter(signal_Node_Code,osmID,
                                           x_coord=signal_Node.xcoord,
                                           y_coord=signal_Node.ycoord,
                                           reference_cycle_length=signal_Node.reference_cycle_length)
        signal_Node_List.Add_Signal_Node(new_Output_Node)
        #for movement
        for m in signal_Node.movement_Array:
            if m.Enable==True:
                signal_Movement_Code = GetMovementCode(movement_Index=m.movementIndex,
                                                       left_Turn_Treatment=m.Left_Turn_Treatment,
                                                       NEMA_Phase=m.NEMA_Phase,
                                                       ring=m.Ring,
                                                       barrier=m.Barrier)
                new_Output_Movement = CSignal_Movement_Inter(movementCode=signal_Movement_Code,
                                                             signal_Node=new_Output_Node,
                                                             stageNo_in_Order=m.StageNo_in_Order,
                                                             groupNo=m.GroupNo,
                                                             directionNo=m.DirectionNo,
                                                             ib_Link_id=m.ib_link_id,
                                                             ob_Link_id=m.ob_link_id,
                                                             lanes=m.Lanes,
                                                             movement_str=m.movementIndex.name,
                                                             volume=m.Volume,
                                                             geometry=m.Geometry,
                                                             ib_osm_node_id=m.ib_osm_node_id,
                                                             ob_osm_node_id=m.ob_osm_node_id,
                                                             osm_node_id=m.osm_node_id,
                                                             node_id=m.node_id)
                signal_Movement_List.Add_Signal_Movement(new_Output_Movement)


    signal_Node_info_List=signal_Node_List.Output_Signal_Node_Info()
    signal_Movement_info_List=signal_Movement_List.Output_Signal_Movement_Info()

    signal_Node_info_List_df=pd.DataFrame(signal_Node_info_List,
                                             columns=["signal_code",
                                                      "osm_node_id",
                                                      "x_coord",
                                                      "y_coord",
                                                      "reference_cycle_length"])
    signal_Movement_info_List_df=pd.DataFrame(signal_Movement_info_List,
                                             columns=["movement_code",
                                                      "signal_node_code",
                                                      "signal_link",
                                                      "stageNo_in_Order",
                                                      "osm_node_id",
                                                      "node_id",
                                                      "groupNo",
                                                      "directionNo",
                                                      "ib_link_id",
                                                      "ob_link_id",
                                                      "ib_osm_node_id",
                                                      "ob_osm_node_id",
                                                      "lanes",
                                                      "mvmt_txt_id",
                                                      "volume",
                                                      "geometry"])
    signal_Node_info_List_df.to_csv(f"signal_node_{str(label_name)}.csv", index=False)
    signal_Movement_info_List_df.to_csv(f"signal_movement_{str(label_name)}.csv", index=False)


def Input_Intermediate_Files(label_name="setting"):
    g_node_map = {}
    internal_node_seq_no=0
    _config_Parameters = Configuration()
    parser_movement = pd.read_csv(f"signal_movement_{str(label_name)}.csv")
    parser = pd.read_csv(f"signal_node_{str(label_name)}.csv",converters = {"osm_node_id":str})

    for i in range(len(parser_movement["movement_code"])):
        movementCode = str(parser_movement["movement_code"][i])
        movementStr = str(parser_movement["mvmt_txt_id"][i])
        osm_node_id= str(parser_movement["osm_node_id"][i])
        node_id = str(parser_movement["node_id"][i])
        stageNo_in_Order = str(parser_movement["stageNo_in_Order"][i])
        mvmt_id=osm_node_id+movementStr
        geometry=parser_movement["geometry"][i]
        ib_link_id=parser_movement["ib_link_id"][i]
        ob_link_id = parser_movement["ob_link_id"][i]
        ib_osm_node_id=parser_movement["ib_osm_node_id"][i] # for timing.csv
        ob_osm_node_id=parser_movement["ob_osm_node_id"][i] #for timing.csv
        initial_volume = parser_movement["volume"][i]
        lanes = parser_movement["lanes"][i]
        # sharedLanes = parser_movement["sharedLanes"][i]
        sharedLanes = 1

        if len(movementStr) > 0 and movementStr != "nan":
            if osm_node_id !="":
                if osm_node_id not in g_node_map.keys():
                    row=parser[parser["osm_node_id"]==osm_node_id]
                    xcoord = row["x_coord"].values[0]
                    ycoord = row["y_coord"].values[0]
                    rcl=row["reference_cycle_length"].values[0]
                    reference_cycle_length = int(rcl) if rcl !="nan" else 0
                    mainModual.g_internal_node_to_seq_no_map[osm_node_id] = internal_node_seq_no
                    internal_node_seq_no+=1
                    mainModual.g_number_of_nodes += 1

                    g_node_map[osm_node_id] = CSignalNode(osm_node_id,
                                                          xcoord,
                                                          ycoord,
                                                          _config_Parameters,
                                                          reference_cycle_length)

                g_node_map[osm_node_id].AddMovementVolume(osm_node_id,
                                                          node_id,
                                                          ib_link_id,
                                                          ob_link_id,
                                                          ib_osm_node_id,
                                                          ob_osm_node_id,
                                                          movementStr,
                                                          initial_volume,
                                                          lanes,
                                                          sharedLanes,
                                                          geometry,
                                                          mvmt_id)
                if stageNo_in_Order != "nan":
                    stageNo_in_Order = stageNo_in_Order.split(",")
                    stageNo_in_Order = [EStage(int(x)) for x in stageNo_in_Order]
                    groupNo = int(parser_movement["groupNo"][i])
                    groupNo = EGroup(groupNo)
                    directionNo = int(parser_movement["directionNo"][i])
                    directionNo = EDirection(directionNo)
                    g_node_map[osm_node_id].AddMovementVolume_Additional(movementStr,stageNo_in_Order,groupNo,directionNo,movementCode)
                g_node_map[osm_node_id].OSM_Node_ID=osm_node_id
                mainModual.g_number_of_movements +=1
    return


#"road_link_id", "from_node_id", "to_node_id",
#"main_node_id",


def set_reference_cycle_length():
    node_data=pd.read_csv(macroNodeFileName)
    if "notes" not in node_data.columns:
        node_data["notes"]=""
    if "reference_cycle_length" not in node_data.columns:
        node_data["reference_cycle_length"]=""
    for i in range(len(node_data["osm_node_id"])):
        ctrl_type = str(node_data["ctrl_type"][i])
        if ctrl_type=="signal" or ctrl_type=="1":
            node_data.loc[i,"notes"]="reference_cycle_length set by default"
            node_data.loc[i,"reference_cycle_length"]=90
    node_data.to_csv(macroNodeFileName,index=False)

def set_default_volume():
    movement_data = pd.read_csv(movementFileName)
    if "notes" not in movement_data.columns:
        movement_data["notes"]=""
    for i in range(len(movement_data["mvmt_txt_id"])):
        movement_str = str(movement_data["mvmt_txt_id"][i])
        lanes=int(movement_data["lanes"][i])
        if "L" in movement_str:
            init_volume = 105 * lanes
        elif "R" in movement_str:
            init_volume = 110 * lanes
        else:
            init_volume = 310 * lanes
        # movement_data["volume"][i]=init_volume
        # movement_data["notes"][i] = "volume set by default"
        movement_data.loc[i, "notes"] = "volume set by default"
        movement_data.loc[i, "volume"]=init_volume
    movement_data.to_csv(movementFileName,index=False)



def determine_major_approach():
    for osmID, signal_Node in g_node_map.items():
        signal_Node.Set_Major_Apporach()
    Output_Intermediate_Files()

def select_left_turn_treatment():
    Input_Intermediate_Files()
    for osmID, signal_Node in g_node_map.items():
        signal_Node.Initialization()
    Output_Intermediate_Files()

def Preset_Phase_Mvmt_File():
    file_path="signal_phase_mvmt.csv"
    if not os.path.exists(file_path):
        return
    phase_mvmt_data=pd.read_csv(file_path)
    index=0
    for node_id, sn in g_node_map.items():
        for m in range(1, movementSize + 1):
            if sn.movement_Array[m].Enable:
                for so in range(len(sn.movement_Array[m].StageNo_in_Order)):
                    mvmt_txt_id=phase_mvmt_data["mvmt_txt_id"][index]
                    signal_phase_num=phase_mvmt_data["signal_phase_num"][index]
                    stage_no=phase_mvmt_data["stage_no"][index]
                    protection=ELeft_Turn_Treatment["prot"] if phase_mvmt_data["protection"][index]=="protected" else ELeft_Turn_Treatment["perm"]

                    sn.movement_Array[m].movementIndex = EMovement_Index[mvmt_txt_id]  # mvmt_txt_id
                    sn.movement_Array[m].NEMA_Phase = E_NEMA_Phase(signal_phase_num)  # signal_phase_num
                    sn.movement_Array[m].StageNo_in_Order[so] = EStage(stage_no)  # stage_no
                    sn.movement_Array[m].mvmt_id = phase_mvmt_data["mvmt_id"][index]  # mvmt_id
                    sn.movement_Array[m].node_id = phase_mvmt_data["node_id"][index]
                    sn.movement_Array[m].osm_node_id = phase_mvmt_data["osm_node_id"][index]
                    sn.movement_Array[m].ib_link_id = phase_mvmt_data["ib_link_id"][index]  # ib_link_id
                    sn.movement_Array[m].ob_link_id = phase_mvmt_data["ib_link_id"][index]  # ib_link_id
                    sn.movement_Array[m].ib_osm_node_id = phase_mvmt_data["ib_osm_node_id"][index]  # ib_osm_node_id
                    sn.movement_Array[m].ob_osm_node_id = phase_mvmt_data["ob_osm_node_id"][index]  # ob_osm_node_id
                    sn.movement_Array[m].Left_Turn_Treatment = protection  # protection
                    sn.movement_Array[m].Geometry = phase_mvmt_data["geometry"][index]  # geometry
                    index+=1


def estimate_signal_timing(input_preset_phase_mvmt_file:bool=False):
    if input_preset_phase_mvmt_file:
        Preset_Phase_Mvmt_File()
    Input_Intermediate_Files()
    for osmID,signal_Node in g_node_map.items():
        signal_Node.timing_process()