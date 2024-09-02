from ovito.data import *
from ovito.io import import_file, export_file
from ovito.modifiers import CommonNeighborAnalysisModifier
from ovito.data import DislocationNetwork
filename = "dump.11ps"

def modify(frame, data):
    
    

 pipeline = import_file("F:/Research/AM/{}".format(filename),columns =["Particle Identifier","Particle Type", "Position.X", "Position.Y", "Position.Z"])

 # Extract dislocation lines from a crystal with diamond structure:
 modifier = CommonNeighborAnalysisModifier()
 #modifier.input_crystal_structure = DislocationAnalysisModifier.Lattice.FCC
 pipeline.modifiers.append(modifier)
 data = pipeline.compute()

 hcp = data.attributes['CommonNeighborAnalysis.counts.HCP']
 bcc = data.attributes['CommonNeighborAnalysis.counts.BCC']
 fcc = data.attributes['CommonNeighborAnalysis.counts.FCC']
 ico = data.attributes['CommonNeighborAnalysis.counts.ICO']
 others = data.attributes['CommonNeighborAnalysis.counts.OTHER']
 #cell_volume = data.attributes['DislocationAnalysis.cell_volume']
 print("{} {} {} {} {}".format(others,fcc,hcp,bcc,ico))

 # Print list of dislocation lines:
# print("Found %i dislocation segments" % len(data.dislocations.segments))
# 
 file= open("F:/Research/AM/"+filename+".txt", 'a+')
 file.write("{} {} {} {} {}\n".format(others,fcc,hcp,bcc,ico))
 file.close()

# Or export dislocations to a ParaView VTK file:
 #export_file(pipeline, "dislocations.vtk", "vtk/disloc"