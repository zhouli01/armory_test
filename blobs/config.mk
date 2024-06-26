#*********************************************************************************************************
#
#                                    中国软件开源组织
#
#                                   嵌入式实时操作系统
#
#                                SylixOS(TM)  LW : long wing
#
#                               Copyright All Rights Reserved
#
#--------------文件信息--------------------------------------------------------------------------------
#
# 文   件   名: config.mk
#
# 创   建   人: RealEvo-IDE
#
# 文件创建日期: 2024 年 04 月 22 日
#
# 描        述: 本文件由 RealEvo-IDE 生成，用于配置 Makefile 功能，请勿手动修改
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
