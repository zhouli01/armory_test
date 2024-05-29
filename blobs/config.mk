#*********************************************************************************************************
#
#                                    �й�������Դ��֯
#
#                                   Ƕ��ʽʵʱ����ϵͳ
#
#                                SylixOS(TM)  LW : long wing
#
#                               Copyright All Rights Reserved
#
#--------------�ļ���Ϣ--------------------------------------------------------------------------------
#
# ��   ��   ��: config.mk
#
# ��   ��   ��: RealEvo-IDE
#
# �ļ���������: 2024 �� 04 �� 22 ��
#
# ��        ��: ���ļ��� RealEvo-IDE ���ɣ��������� Makefile ���ܣ������ֶ��޸�
#*********************************************************************************************************

#*********************************************************************************************************
# SylixOS Base Project path
#*********************************************************************************************************
SYLIXOS_BASE_PATH := ..

#*********************************************************************************************************
# Toolchain prefix
#*********************************************************************************************************
TOOLCHAIN_PREFIX := arm-sylixos-eabi-

#*********************************************************************************************************
# Debug options (debug or release)
#*********************************************************************************************************
DEBUG_LEVEL := debug

#*********************************************************************************************************
# NOTICE: libsylixos, BSP and other kernel modules projects CAN NOT use vfp!
#*********************************************************************************************************
FPU_TYPE := 
CPU_TYPE := 

#*********************************************************************************************************
# Multi-platform build
#*********************************************************************************************************
MULTI_PLATFORM_BUILD := yes

#*********************************************************************************************************
# Platforms(See SylixOS Base/platforms.mk to get more platform's name)
#*********************************************************************************************************
PLATFORMS := ARM_926H MIPS64_R2_SOFT X86_64 X86_641 X86_642

#*********************************************************************************************************
# End
#*********************************************************************************************************