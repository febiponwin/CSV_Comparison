import ezdxf
import matplotlib.pyplot as plt

# Open the DXF file
dwg = ezdxf.readfile("file.dxf")

# Get the modelspace
modelspace = dwg.modelspace()

# Get all the POLYLINE entities in modelspace
polylines = modelspace.query('DXFType("POLYLINE")')

# Plot the polylines
for polyline in polylines:
    vertices = polyline.vertices()
    x = [vertex[0] for vertex in vertices]
    y = [vertex[1] for vertex in vertices]
    plt.plot(x, y)

# Get all the TEXT entities in modelspace
texts = modelspace.query('DXFType("TEXT")')

# Plot the texts
for text in texts:
    x = text.dxf.insert[0]
    y = text.dxf.insert[1]
    plt.text(x, y, text.dxf.text)

# Show the plot
plt.show()
