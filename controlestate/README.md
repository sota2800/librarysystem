﻿# controlestate

## Overview

ModuleDescription

## Description



### Input and Output



### Algorithm etc



### Basic Information

|  |  |
----|---- 
| Module Name | controlestate |
| Description | ModuleDescription |
| Version | 1.0.0 |
| Vendor | VenderName |
| Category | Category |
| Comp. Type | STATIC |
| Act. Type | PERIODIC |
| Kind | DataFlowComponent |
| MAX Inst. | 1 |

### Activity definition

<table>
  <tr>
    <td rowspan="4">on_initialize</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td>on_finalize</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_startup</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_shutdown</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_activated</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_deactivated</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td rowspan="4">on_execute</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td>on_aborting</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_error</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_reset</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_state_update</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_rate_changed</td>
    <td colspan="2"></td>
  </tr>
</table>

### InPorts definition


### OutPorts definition

#### controlesota



<table>
  <tr>
    <td>DataType</td>
    <td>RTC::TimedString</td>
    <td></td>
  </tr>
  <tr>
    <td>IDL file</td>
    <td colspan="2">BasicDataType.idl</td>
  </tr>
  <tr>
    <td>Number of Data</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Semantics</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Unit</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Occirrence frecency Period</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Operational frecency Period</td>
    <td colspan="2"></td>
  </tr>
</table>

#### callstaff



<table>
  <tr>
    <td>DataType</td>
    <td>RTC::TimedBoolean</td>
    <td></td>
  </tr>
  <tr>
    <td>IDL file</td>
    <td colspan="2">BasicDataType.idl</td>
  </tr>
  <tr>
    <td>Number of Data</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Semantics</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Unit</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Occirrence frecency Period</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Operational frecency Period</td>
    <td colspan="2"></td>
  </tr>
</table>

#### log



<table>
  <tr>
    <td>DataType</td>
    <td>RTC::TimedString</td>
    <td></td>
  </tr>
  <tr>
    <td>IDL file</td>
    <td colspan="2">BasicDataType.idl</td>
  </tr>
  <tr>
    <td>Number of Data</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Semantics</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Unit</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Occirrence frecency Period</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Operational frecency Period</td>
    <td colspan="2"></td>
  </tr>
</table>


### Service Port definition

#### facedetectionconsumer



<table>
  <tr>
    <td>I/F Description</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td colspan="3">Interface</td>
  </tr>
  <tr>
    <td rowspan="9">facedetectiondata</td>
    <td>Type</td>
    <td>Library::facedetectiondata</td>
    <tr>
      <td>Direction</td>
      <td>Consumer</td>
    </tr>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>IDL file</td>
      <td>facedetection.idl</td>
    </tr>
    <tr>
      <td>Argument</td>
      <td></td>
    </tr>
    <tr>
      <td>Return Value</td>
      <td></td>
    </tr>
    <tr>
      <td>Exception</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
</table>

#### selectconusmer



<table>
  <tr>
    <td>I/F Description</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td colspan="3">Interface</td>
  </tr>
  <tr>
    <td rowspan="9">selectdata</td>
    <td>Type</td>
    <td>Library::selectdata</td>
    <tr>
      <td>Direction</td>
      <td>Consumer</td>
    </tr>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>IDL file</td>
      <td>select.idl</td>
    </tr>
    <tr>
      <td>Argument</td>
      <td></td>
    </tr>
    <tr>
      <td>Return Value</td>
      <td></td>
    </tr>
    <tr>
      <td>Exception</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
</table>

#### voicerecogconsumer



<table>
  <tr>
    <td>I/F Description</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td colspan="3">Interface</td>
  </tr>
  <tr>
    <td rowspan="9">voicerecogdata</td>
    <td>Type</td>
    <td>Library::voicerecogdata</td>
    <tr>
      <td>Direction</td>
      <td>Consumer</td>
    </tr>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>IDL file</td>
      <td>voicerecog.idl</td>
    </tr>
    <tr>
      <td>Argument</td>
      <td></td>
    </tr>
    <tr>
      <td>Return Value</td>
      <td></td>
    </tr>
    <tr>
      <td>Exception</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
</table>

#### seleniumconsumer



<table>
  <tr>
    <td>I/F Description</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td colspan="3">Interface</td>
  </tr>
  <tr>
    <td rowspan="9">seleniumdata</td>
    <td>Type</td>
    <td>Library::seleniumdata</td>
    <tr>
      <td>Direction</td>
      <td>Consumer</td>
    </tr>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>IDL file</td>
      <td>selenium.idl</td>
    </tr>
    <tr>
      <td>Argument</td>
      <td></td>
    </tr>
    <tr>
      <td>Return Value</td>
      <td></td>
    </tr>
    <tr>
      <td>Exception</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
</table>


### Configuration definition


## Demo

## Requirement

## Setup

### Windows

### Ubuntu

## Usage

## Running the tests

## LICENCE




## References




## Author

