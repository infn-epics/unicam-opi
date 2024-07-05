from org.csstudio.display.builder.runtime.script import ScriptUtil,PVUtil

import os
from java.lang import Exception
logger = ScriptUtil.getLogger()


conffile = PVUtil.getString(pvs[0]) ## Expects FileName as first parameter
logger.info("LOAD Devices, Device file "+conffile + " PV: "+str(pvs[0]))

if not os.path.exists(conffile):
    opihome=os.getenv("OPIHOME",".")
    ini=opihome+"/ini"
    conffile=ini+"/"+conffile

if not os.path.exists(conffile):
    ScriptUtil.showMessageDialog(widget,"Cannot find  file \""+conffile+"\" please set CONFILE macro to a correct file")

    
motorf = os.path.abspath(conffile)

logger.info("LOAD opening "+conffile )
combo = ScriptUtil.findWidgetByName(widget, "DeviceCombo")
# axis = ScriptUtil.findWidgetByName(widget, "TML_AXIS")

# Initialize an empty list to store the values
device_list = []

# Open the file and read values into the list
with open(motorf, 'r') as file:
    for line in file:
        # Strip whitespace characters (like newline) from each line
        stripped_line = line.strip()
        if stripped_line:  # Avoid adding empty lines
            logger.info("loading " +stripped_line )
            device_list.append(stripped_line)


combo.setItems(device_list)
#if len(device_list) > 0:
    #device_macro= axis.getPropertyValue("macros")
    #device_macro.add("DEVICE", device_prefix + device_list[0])
    # axis.setPropertyValue("file","")
    # axis.setPropertyValue("file","TML_Main.bob")

