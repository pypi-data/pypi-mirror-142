import pythreejs as THREE
import numpy as np
from IPython.display import display
from compas.colors import Color
from compas.datastructures import Mesh
from compas.datastructures import Network
from compas.geometry import Shape


class App():

    def __init__(self, width=800, height=600, background: Color = Color.white()):

        camera_light = THREE.DirectionalLight(color='white', position=[3, 5, 1], intensity=0.5)
        self.camera = THREE.PerspectiveCamera(position=[5, 5, 5], up=[0, 0, 1], children=[camera_light])

        ambient_light = THREE.AmbientLight(color='#777777')
        self.scene = THREE.Scene(children=[ambient_light, self.camera])

        self.controls = THREE.OrbitControls(
            controlling=self.camera,
            minAzimuthAngle=-100000.0,
            maxAzimuthAngle=100000.0,
            maxDistance=100000.0,
            maxZoom=1000000)

        self.renderer = THREE.Renderer(
            camera=self.camera,
            scene=self.scene,
            controls=[self.controls],
            background=background.hex,
            width=width,
            height=height
        )

    def add(self, item, *args, **kwargs):
        item = self.to_threejs(item, *args, **kwargs)
        self.scene.add(item)

    def to_threejs(self, item,
                   facecolor: Color = Color.white(), pointcolor: Color = Color.black(), linecolor: Color = Color.grey(),
                   show_points: bool = False, show_lines: bool = True, show_faces: bool = True,
                   pointsize: float = 1, linewidth: float = 1, opacity: float = 1):

        if isinstance(item, Mesh):
            mesh = item
            vertex_attributes = mesh.vertex_attributes
            vertex = mesh.vertex
        elif isinstance(item, Shape):
            mesh = Mesh.from_shape(item)
            vertex_attributes = mesh.vertex_attributes
            vertex = mesh.vertex
        elif isinstance(item, Network):
            mesh = item
            vertex_attributes = mesh.node_attributes
            vertex = mesh.node
            show_faces = False
            show_points = True

        else:
            raise Exception('Unsupported item type:', type(item))

        vertices = []

        if show_faces:
            for face in mesh.face:
                face_vertices = mesh.face_vertices(face)
                if len(face_vertices) == 3:
                    for v in face_vertices:
                        xyz = vertex_attributes(v, 'xyz')
                        vertices.append(xyz)
                elif len(face_vertices) == 4:
                    face_vertices = face_vertices[:3] + face_vertices[2:] + face_vertices[0:1]
                    for v in face_vertices:
                        xyz = vertex_attributes(v, 'xyz')
                        vertices.append(xyz)
                else:
                    raise ValueError('Only triangular and quad faces are supported.')

        vertices = THREE.BufferAttribute(
            array=np.array(vertices, dtype=np.float32), normalized=False)

        geometry = THREE.BufferGeometry(attributes={'position': vertices})
        geometry.exec_three_obj_method('computeVertexNormals')

        if opacity < 1:
            material = THREE.MeshPhongMaterial(color=facecolor.hex, side='DoubleSide', opacity=opacity, transparent=True)
        else:
            material = THREE.MeshPhongMaterial(color=facecolor.hex, side='DoubleSide')

        three_mesh = THREE.Mesh(geometry=geometry, material=material)

        if show_points:
            vertices = []
            for v in vertex:
                xyz = vertex_attributes(v, 'xyz')
                vertices.append(xyz)

            vertices = THREE.BufferAttribute(
                array=np.array(vertices, dtype=np.float32), normalized=False)

            geometry = THREE.BufferGeometry(attributes={'position': vertices})
            three_mesh.add(THREE.Points(geometry, THREE.PointsMaterial(color=pointcolor.hex, size=pointsize)))

        if show_lines:
            vertices = []
            for edge in mesh.edges():
                start = vertex_attributes(edge[0], 'xyz')
                end = vertex_attributes(edge[1], 'xyz')
                vertices.append([start, end])

            geometry = THREE.LineSegmentsGeometry(positions=vertices)
            three_mesh.add(THREE.LineSegments2(geometry, THREE.LineMaterial(color=linecolor.hex, linewidth=linewidth)))

        return three_mesh

    def show(self):
        display(self.renderer)
