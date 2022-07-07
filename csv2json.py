import csv
import json


tools = []

with open('/Users/tors10/Development/fmi-standard.org/_data/tools.csv', newline='') as csvfile:

    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    for row in spamreader:

        if row[0] in ['DS - FMU Export from Simulink', 'HIFSuite', 'JModelica.org', 'Test-FMUs']:
            continue  # discontinued

        # 6               7               8               9               10              11              12              13
        # export_cs_fmi1, export_cs_fmi2, export_me_fmi1, export_me_fmi2, import_cs_fmi1, import_cs_fmi2, import_me_fmi1, import_me_fmi2

        fmi_versions = []
        fmu_export = []
        fmu_import = []

        if row[6] == 'available' or row[8] == 'available' or row[10] == 'available' or row[12] == 'available':
            fmi_versions.append('1.0')

        if row[7] == 'available' or row[9] == 'available' or row[11] == 'available' or row[13] == 'available':
            fmi_versions.append('2.0')

        features = []

        if row[6] == 'available' or row[7] == 'available':
            fmu_export.append('CS')

        if row[8] == 'available' or row[9] == 'available':
            fmu_export.append('ME')

        if row[10] == 'available' or row[11] == 'available':
            fmu_import.append('CS')

        if row[12] == 'available' or row[13] == 'available':
            fmu_import.append('ME')

        platforms = []

        if 'darwin64' in row[5]:
            platforms.append('macOS')

        if 'linux64' in row[5]:
            platforms.append('Linux')

        if 'win64' in row[5]:
            platforms.append('Windows')

        name = row[0]
        url = row[2]
        version = None
        logo = None
        vendor = None
        vendorURL = row[2]

        s = name.split(' ')

        if name == '20-sim':
            name = name
            vendor = "Controllab Products"
        elif name == '@Source':
            name = name
            vendor = 'Podium Technology'
            vendorURL = "https://podiumtechnology.co.uk/"
        elif name == 'Adams':
            name = name
            vendor = 'MSC Software'
            vendorURL = "https://www.mscsoftware.com/"
        elif name == 'AutoFOCUS3 (AF3)':
            name = 'AutoFOCUS3'
            vendor = 'fortiss'
            vendorURL = "https://www.fortiss.org/en/"
        elif name == 'AUTOSAR Builder':
            name = name
            # logo = '3DS.svg'
            vendor = 'Dassault Systèmes'
            vendorURL = "https://3ds.com/"
        elif name == 'Axisuite':
            name = 'exothermia suite'
            vendor = 'Exothermia'
            vendorURL = "http://exothermia.com/"
        elif name == 'BEAST':
            name = name
            vendor = 'SKF'
            vendorURL = "https://www.skf.com/"
        elif name == 'CANoe':
            name = name
            vendor = 'Vector'
            vendorURL = "https://www.vector.com/"
        elif name == 'CarMaker':
            name = name
            vendor = 'IPG Automotive'
            vendorURL = "https://ipg-automotive.com/"
        elif name == 'CarSim':
            name = name
            vendor = 'Mechanical Simulation'
            vendorURL = 'https://www.carsim.com/'
        elif name == 'CATIA':
            name = name
            # logo = '3DS.svg'
            vendor = 'Dassault Systèmes'
            vendorURL = "https://3ds.com/"
        elif name == 'ControlBuild':
            name = name
            # logo = '3DS.svg'
            vendor = 'Dassault Systèmes'
            vendorURL = "https://3ds.com/"
        elif name == 'CosiMate':
            name = name
            vendor = 'ChiasTek'
            vendorURL = 'https://www.chiastek.com/'
        elif name == 'CoTherm':
            name = name
            vendor = 'ThermoAnalytics'
            vendorURL = 'https://www.thermoanalytics.com/'
        elif name == 'CPPFMU':
            name = name
            vendor = 'ViProMa'
            vendorURL = 'https://viproma.no/'
        elif name == 'DACCOSIM':
            name = name
            vendor = 'DACCOSIM'
            vendorURL = 'https://bitbucket.org/simulage/daccosim'
        elif name == 'DAE Tools':
            name = name
            vendor = 'DAE Tools'
            vendorURL = 'https://www.daetools.com'
        elif name == 'DAFUL':
            name = 'Motion'
            url = 'https://www.ansys.com/ko-kr/products/structures/ansys-motion'
            # logo = 'Ansys.svg'
            vendor = 'Ansys'
            vendorURL = 'https://www.ansys.com/'
        elif name == 'DS - FMU Import into Simulink':
            name = 'FMI Kit for Simulink'
            url = 'https://github.com/CATIA-Systems/FMIKit-Simulink'
            # logo = '3DS.svg'
            vendor = 'Dassault Systèmes'
            vendorURL = "https://3ds.com/"
        elif name == 'Dymola':
            name = name
            version = '2023'
            # logo = '3DS.svg'
            vendor = 'Dassault Systèmes'
            vendorURL = "https://3ds.com/"
        elif name == 'DYNA4':
            name = name
            vendor = 'Vector'
            vendorURL = 'https://www.vector.com/'
        elif name == 'EAS-CoSiMa':
            name = name
            vendor = 'Fraunhofer IIS'
            vendorURL = 'https://www.eas.iis.fraunhofer.de/'
        elif name == 'Easy FMI Add-on for Matlab/Simulink':
            name = name
            vendor = 'Powersys Solutions'
            vendorURL = 'https://powersys-solutions.com/'
        elif name == 'Easy5':
            name = name
            vendor = 'MSC Software'
            vendorURL = "https://www.mscsoftware.com/"
        elif name == 'EcosimPro':
            name = name
            vendor = 'EA Internacional'
            vendorURL = 'https://www.empresariosagrupados.es/'
        elif name == 'ECU-TEST':
            name = name
            # logo = 'TraceTronic.png'
            vendor = 'TraceTronic'
            vendorURL = 'https://www.tracetronic.com/'
        elif name == 'EMTP-RV':
            name = 'EMTP'
            vendor = 'EMTP Alliance'
            vendorURL = 'https://www.emtp.com/'
        elif name == 'EnergyPlus':
            name = name
            vendor = 'Berkeley Lab'
            vendorURL = 'https://www.lbl.gov/'
        elif name == 'Flownex':
            name = name
            vendor = 'Flownex'
            vendorURL = url
        elif name == 'FMI Add-in for Excel':
            name = name
            # logo = 'Modelon.png'
            vendor = 'Modelon'
            vendorURL = 'https://www.modelon.com/'
        elif name == 'FMI add-on for NI VeriStand':
            name = name
            vendor = 'DOFWARE'
            vendorURL = 'https://www.dofware.com/'
        elif name == 'FMI Bench':
            name = name
            # logo = 'PMSF.png'
            vendor = 'PMSF IT Consulting'
            vendorURL = 'https://pmsf.eu/'
        elif name == 'FMI Blockset for Simulink':
            name = name
            vendor = 'Claytex'
            vendorURL = 'https://www.claytex.com/'
        elif name == 'FMI Composer':
            name = name
            # logo = 'Modelon.png'
            vendor = 'Modelon'
            vendorURL = 'https://www.modelon.com/'
        elif name == 'FMI Library':
            name = name
            # logo = 'Modelon.png'
            vendor = 'Modelon'
            vendorURL = 'https://www.modelon.com/'
        elif name == 'FMI Target for Simulink Coder':
            name = name
            # logo = 'ESI.svg'
            vendor = 'ESI Group'
            vendorURL = 'https://www.esi-group.com/'
        elif name == 'FMI Toolbox for MATLAB/Simulink':
            name = name
            # logo = 'Modelon.png'
            vendor = 'Modelon'
            vendorURL = 'https://www.modelon.com/'
        elif name == 'FMI.jl':
            name = name
            vendor = '@ThummeTo'
            vendorURL = 'https://github.com/ThummeTo/'
        elif name == 'FMI4cpp':
            name = name
            vendor = 'NTNU'
            vendorURL = 'https://www.ntnu.edu/ihb'
        elif name == 'FMI4j':
            name = name
            vendor = 'NTNU'
            vendorURL = 'https://www.ntnu.edu/ihb'
        elif name == 'FMPy':
            name = name
            # logo = '3DS.svg'
            vendor = 'Dassault Systèmes'
            vendorURL = "https://3ds.com/"
        elif name == 'FMU-proxy':
            name = name
            vendor = 'NTNU'
            vendorURL = 'https://www.ntnu.edu/ihb'
        elif name == 'FMUSDK':
            name = 'FMU SDK'
            vendor = 'Synopsys'
            vendorURL = 'https://www.synopsys.com/'
        elif name == 'GCAir':
            name = name
            vendor = 'Global Crown'
            vendorURL = 'http://www.globalcrown.com.cn/'
        elif name == 'GCKontrol':
            name = name
            vendor = 'Global Crown'
            vendorURL = 'http://www.globalcrown.com.cn/'
        elif name == 'General Energy Systems':
            name = name
            vendor = 'TNO'
            vendorURL = 'https://www.tno.nl'
        elif name == 'GT-SUITE':
            name = name
            vendor = 'Gamma Technologies'
            vendorURL = 'https://www.gtisoft.com/'
        elif name == 'Hopsan':
            name = name
            vendor = 'LIU'
            vendorURL = 'https://liu.se/en/research/hopsan'
        elif name == 'ICOS':
            name = name
            vendor = 'Virtual Vehicle'
            vendorURL = 'https://www.v2c2.at/'
        elif name == 'IGNITE':
            vendor = 'Ricardo'
            vendorURL = 'https://ricardo.com/'
        elif name == 'InSystemLab':
            name = name
            vendor = 'E-Sim Solutions'
            vendorURL = 'https://www.esims.tech/'
        elif name == 'INTO-CPS':
            name = name
            vendor = 'INTO-CPS'
            vendorURL = 'https://into-cps.org/'
        elif name == 'ISG-virtuos':
            name = name
            vendor = 'ISG'
            vendorURL = 'https://www.isg-stuttgart.de/'
        elif name == 'JavaFMI':
            name = name
            vendor = '@siani'
            vendorURL = 'https://bitbucket.org/siani/'
        elif name == 'JFMI':
            name = name
            vendor = 'The Ptolemy Project'
            vendorURL = 'https://ptolemy.berkeley.edu/'
        elif name == 'KULI':
            name = name
            vendor = 'Magna'
            vendorURL = 'https://www.magna.com/'
        elif name == 'LS-DYNA':
            name = name
            vendor = 'LST'
            vendorURL = 'http://www.lstc.com/'
        elif name == 'MapleSim':
            name = name
            # logo = 'Maplesoft.svg'
            vendor = 'Maplesoft'
            vendorURL = 'https://www.maplesoft.com/'
        elif name == 'MasterSim':
            name = name
            vendor = 'Bauklimatik Dresden Software'
            vendorURL = 'https://bauklimatik-dresden.de/'
        elif name == 'MATLAB® Simulink®':
            name = name
            # logo = 'MathWorks.svg'
            vendor = 'MathWorks'
            vendorURL = 'https://www.mathworks.com/'
        elif name == 'MESSINA':
            name = name
            vendor = 'Expleo'
            vendorURL = 'https://expleo.com/'
        elif name == 'MoBA Lab':
            name = 'MoBA Automation'
            url = 'https://www.tlk-thermo.com/index.php/en/moba-automation'
            vendor = 'TLK-Thermo'
            vendorURL = 'https://www.tlk-thermo.com/'
        elif name == 'modeFRONTIER':
            name = name
            vendor = 'ESTECO'
            vendorURL = 'https://www.esteco.com/'
        elif name == 'MORPHEE':
            name = name
            url = 'https://www.fev-sts.com/software/test-system-automation/morphee.html'
            vendor = 'FEV'
            vendorURL = 'https://www.fev-sts.com/'
        elif name == 'MpCCI CouplingEnvironment':
            name = name
            vendor = 'Fraunhofer SCAI'
        elif name == 'MWorks':
            name = name
            vendor = 'Tongyuan'
        elif name == 'NANDRAD Solver':
            name = 'NANDRAD'
            vendor = 'Bauklimatik Dresden Software'
            vendorURL = 'https://bauklimatik-dresden.de/'
        elif name == 'OMSimulator':
            name = name
            vendor = 'OpenModelica'
            vendorURL = 'https://openmodelica.org/'
        elif name == 'Open Simulation Platform':
            name = name
            vendor = 'Open Simulation Platform'
        elif name == 'OpenModelica':
            name = name
            vendor = 'OpenModelica'
            vendorURL = 'https://openmodelica.org/'
        elif name == 'OPTIMICA Compiler Toolkit':
            name = name
            # logo = 'Modelon.png'
            vendor = 'Modelon'
            vendorURL = 'https://www.modelon.com/'
        elif name == 'optiSLang':
            name = name
            url = 'https://www.ansys.com/products/connect/ansys-optislang'
            # logo = 'Ansys.svg'
            vendor = 'Ansys'
            vendorURL = 'https://www.ansys.com/'
        elif name == 'Overture':
            vendor = 'The Overture Project'
        elif name == 'pandapower-fmu':
            name = 'pandapower-FMU'
            url = ''
            vendor = '@Adrien.Gougeon'
            vendorURL = 'https://framagit.org/Adrien.Gougeon'
        elif name == 'Persalys':
            vendor = 'Persalys'
        elif name == 'PLECS':
            vendor = 'Plexim'
        elif name == 'PragmaDev Studio':
            vendor = 'PragmaDev'
        elif name == 'PROOSIS':
            vendor = 'EA Internacional'
            vendorURL = 'https://www.empresariosagrupados.es/'
        elif name == 'PROVEtech:RE':
            vendor = 'PROVEtech'
            vendorURL = 'https://www.provetech.de/'
        elif name == 'pSeven':
            vendor = 'DATADVANCE'
            vendorURL = 'https://www.datadvance.net/'
        elif name == 'PSIM':
            vendor = 'Powersim'
            vendorURL = 'https://powersimtech.com/'
        elif name == 'Ptolemy II':
            url = 'https://ptolemy.berkeley.edu/ptolemyII/index.htm'
            vendor = 'The Ptolemy Project'
            vendorURL = 'https://ptolemy.berkeley.edu/'
        elif name == 'PyFMI':
            # logo = 'Modelon.png'
            vendor = 'Modelon'
            vendorURL = 'https://www.modelon.com/'
        elif name == 'PySimulator':
            vendor = '@PySimulator'
            vendorURL = 'https://github.com/PySimulator/'
        elif name == 'PythonFMU':
            vendor = 'NTNU'
            vendorURL = 'https://www.ntnu.edu/ihb'
        elif name == 'RecurDyn':
            vendor = 'FunctionBay'
            vendorURL = 'https://functionbay.com/'
        elif name == 'Romax Nexus':
            vendor = 'Romax'
            vendorURL = 'https://www.romaxtech.com/'
        elif name == 'RTMaps':
            vendor = 'Intempora'
            vendorURL = 'https://intempora.com/'
        elif name == 'SaberEXP':
            vendor = 'Synopsys'
            vendorURL = 'https://www.synopsys.com/'
        elif name == 'SaberRD':
            vendor = 'Synopsys'
            vendorURL = 'https://www.synopsys.com/'
        elif name == 'SCANeR Studio':
            vendor = 'AVSimulation'
            vendorURL = 'https://www.avsimulation.fr'
        elif name == 'scFLOW':
            vendor = 'Sofware Cradle'
            vendorURL = 'https://www.cradle-cfd.com/'
        elif name == 'Scilab/Xcos FMU wrapper':
            # logo = 'ESI.svg'
            vendor = 'ESI Group'
            vendorURL = 'https://www.esi-group.com/'
        elif name == 'scSTREAM':
            vendor = 'Sofware Cradle'
            vendorURL = 'https://www.cradle-cfd.com/'
        elif name == 'Silver':
            vendor = 'Synopsys'
            vendorURL = 'https://www.synopsys.com/'
        elif name == 'SIM-VICUS':
            vendor = 'TU Dresden'
        elif name == 'Simcenter 3D Motion':
            # logo = 'Siemens.svg'
            vendor = 'Siemens'
            vendorURL = 'https://www.siemens.com/'
        elif name == 'Simcenter Amesim':
            # logo = 'Siemens.svg'
            vendor = 'Siemens'
            vendorURL = 'https://www.siemens.com/'
        elif name == 'Simcenter FLOEFD':
            # logo = 'Siemens.svg'
            vendor = 'Siemens'
            vendorURL = 'https://www.siemens.com/'
        elif name == 'Simcenter Flomaster':
            # logo = 'Siemens.svg'
            vendor = 'Siemens'
            vendorURL = 'https://www.siemens.com/'
        elif name == 'Simcenter STAR-CCM+':
            # logo = 'Siemens.svg'
            vendor = 'Siemens'
            vendorURL = 'https://www.siemens.com/'
        elif name == 'SimGrid-FMI':
            vendor = 'SimGrid'
            vendorURL = 'https://simgrid.org/'
        elif name == 'SIMIT Simulation Platform':
            name = 'SIMIT'
            # logo = 'Siemens.svg'
            vendor = 'Siemens'
            vendorURL = 'https://www.siemens.com/'
        elif name == 'SimWB':
            vendor = 'Concurrent Real-Time'
            vendorURL = 'https://concurrent-rt.com/'
        elif name == 'SimulationX':
            # logo = 'ESI.svg'
            vendor = 'ESI Group'
            vendorURL = 'https://www.esi-group.com/'
        elif name == 'SIMULIA Simpack':
            name = 'SIMPACK'
            # logo = '3DS.svg'
            vendor = 'Dassault Systèmes'
            vendorURL = "https://3ds.com/"
        elif name == 'Simulix':
            vendor = '@kvixen'
            vendorURL = 'https://github.com/kvixen/'
        elif name == 'Squish GUI Tester':
            vendor = 'froglogic'
            vendorURL = 'https://www.froglogic.com/'
        elif name == 'Sulca':
            vendor = 'Simantics'
            vendorURL = 'https://www.simantics.org/'
        elif name == 'SystemModeler':
            vendor = 'Wolfram'
            # logo = 'Wolfram.svg'
            vendorURL = 'https://www.wolfram.com/'
        elif name == 'TAITherm':
            vendor = 'ThermoanAlytics'
            vendorURL = 'https://www.thermoanalytics.com/'
        elif name == 'TLK Energy Apps':
            vendor = 'TLK-Thermo'
            vendorURL = 'https://www.tlk-thermo.com/'
        elif name == 'TLK FMI Suite':
            vendor = 'TLK-Thermo'
            vendorURL = 'https://www.tlk-thermo.com/'
        elif name == 'TLK TISC Suite':
            vendor = 'TLK-Thermo'
            vendorURL = 'https://www.tlk-thermo.com/'
        elif name == 'TPT':
            vendor = 'PikeTec'
        elif name == 'TRNSYS FMU Export Utility':
            url = 'https://sourceforge.net/projects/trnsys-fmu/'
            vendor = 'Edmund Widl'
            vendorURL = 'https://sourceforge.net/u/widle/profile/'
        elif name == 'TWT Co-Simulation Framework':
            vendor = 'TWT'
            vendorURL = 'https://twt-gmbh.de/'
        elif name == 'Typhoon HIL':
            vendor = 'Typhoon HIL'
        elif name == 'U-TEST®':
            vendor = 'Spherea'
            vendorURL = 'https://www.spherea.com/'
        elif name == 'VALDYN':
            vendor = 'Ricardo'
            vendorURL = 'https://ricardo.com/'
        elif name == 'VenetDCP':
            vendor = 'Toshiba'
            # logo = 'Toshiba.svg'
            vendorURL = 'https://global.toshiba/'
        elif name == 'Virtual Engine':
            vendor = 'FEV'
            vendorURL = 'https://www.fev-sts.com/'
        elif name == 'VOLTA':
            vendor = 'ESTECO'
            vendorURL = 'https://www.esteco.com/'
        elif name == 'WAVE-RT':
            vendor = 'Ricardo'
            vendorURL = 'https://ricardo.com/'
        elif name == 'WinMOD System':
            name = 'WinMOD'
            vendor = 'WinMOD'
            vendorURL = 'https://www.winmod.de/'
        elif name == 'XFlow':
            # logo = '3DS.svg'
            vendor = 'Dassault Systèmes'
            vendorURL = "https://3ds.com/"
        elif name == 'Cameo Simulation Toolkit (MagicDraw plugin)':
            name = 'Cameo Systems Modeler'
            url = 'https://www.3ds.com/products-services/catia/products/no-magic/cameo-systems-modeler/'
            # logo = '3DS.svg'
            vendor = 'Dassault Systèmes'
            vendorURL = "https://3ds.com/"
        elif name == 'xMOD':
            url = 'https://xmod.fev.com/'
            vendor = 'FEV'
            vendorURL = 'https://www.fev-sts.com/'
        elif name == 'YAKINDU Statechart Tools':
            vendor = 'itemis'
            vendorURL = 'https://www.itemis.com/'
        elif len(s) > 1:
            vendor = s[0]
            name = ' '.join(s[1:])

        tool = {
            'name': name,
            'license': row[4],
            'url': url,
            'vendor': vendor,
            'vendorURL': vendorURL,
            'description': row[3],
            'features': features,
            'platforms': platforms,
            'fmiVersions': fmi_versions,
            'fmuExport': fmu_export,
            'fmuImport': fmu_import,
        }

        if tool['vendor'] in ['ANSYS', 'Ansys']:
            # tool['logo'] = 'Ansys.svg'
            tool['vendor'] = 'Ansys'
            tool['vendorURL'] = 'https://www.ansys.com/'

        if tool['vendor'] == 'Altair':
            # tool['logo'] = 'Altair.svg'
            tool['vendorURL'] = 'https://www.altair.com/'

        # if tool['vendor'] == 'Ricardo':
        #     tool['logo'] = 'Ricardo.svg'

        if tool['vendor'] == 'AVL':
            # tool['logo'] = 'AVL.svg'
            tool['vendorURL'] = 'https://avl.com/'

        # if tool['vendor'] == 'IBM':
        #     tool['logo'] = 'IBM.svg'
        #
        # if tool['vendor'] == 'Modelon':
        #     tool['logo'] = 'Modelon.png'
        #
        # if tool['vendor'] == 'XRG':
        #     tool['logo'] = 'XRG.png'
        #
        # if tool['vendor'] == 'FEV':
        #     tool['logo'] = 'FEV.svg'
        #
        # if tool['vendor'] == 'IPG Automotive':
        #     tool['logo'] = 'IPG.jpeg'
        #
        # if tool['vendor'] == 'Synopsys':
        #     tool['logo'] = 'Synopsys.svg'
        #
        # if tool['vendor'] == 'dSPACE':
        #     tool['logo'] = 'dSPACE.svg'
        #
        # if tool['vendor'] == 'MSC Software':
        #     tool['logo'] = 'MSC.svg'
        #
        # if tool['vendor'] == 'Vector':
        #     tool['logo'] = 'Vector.svg'
        #
        # if tool['vendor'] == 'TLK-Thermo':
        #     tool['logo'] = 'TLK-Thermo.svg'
        #
        # if tool['vendor'] == 'Magna':
        #     tool['logo'] = 'Magna.svg'
        #
        # if tool['vendor'] == 'ETAS':
        #     tool['logo'] = 'ETAS.svg'
        #     tool['vendorURL'] = 'https://www.etas.com/'
        #
        # if tool['name'] == 'SIMPACK':
        #     logo = 'SIMPACK.png'
        #
        # if tool['name'] == 'Dymola':
        #     logo = 'Dymola.png'
        #
        # if tool['name'] == 'OMSimulator':
        #     logo = 'OpenModelica.png'
        #
        # if tool['name'] == 'OpenModelica':
        #     logo = 'OpenModelica.png'
        #
        # if version is not None:
        #     tool['version'] = version
        #
        # if logo is not None:
        #     tool['logo'] = logo

        tools.append(tool)


# print(json.dumps(tools, indent=4))

filtered = []

for tool in tools:
    if tool['fmiVersions']:
        filtered.append(tool)
    else:
        print(tool)

# tools = list(filter(lambda tool: tool['fmiVersions'], tools))

with open("/Users/tors10/Development/fmi-standard.org/assets/tools.json", "w") as file:
    json.dump(filtered, file, indent=4)

print(len(filtered))


