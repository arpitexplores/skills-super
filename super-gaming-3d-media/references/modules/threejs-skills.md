## Module: Threejs Skills
---
name: threejs-skills
description: "Create 3D scenes, interactive experiences, and visual effects using Three.js. Use when user requests 3D graphics, WebGL experiences, 3D visualizations, animations, or interactive 3D elements."
risk: safe
source: "https://github.com/CloudAI-X/threejs-skills"
date_added: "2026-02-27"
---

# Three.js Skills

Systematically create high-quality 3D scenes and interactive experiences using Three.js best practices.

## When to Use

- Requests 3D visualizations or graphics ("create a 3D model", "show in 3D")
- Wants interactive 3D experiences ("rotating cube", "explorable scene")
- Needs WebGL or canvas-based rendering
- Asks for animations, particles, or visual effects
- Mentions Three.js, WebGL, or 3D rendering
- Wants to visualize data in 3D space

## Core Setup Pattern

### 1. Essential Three.js Imports

Always use the correct CDN version (r128):

```javascript
import * as THREE from "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js";
```

**CRITICAL**: Do NOT use example imports like `THREE.OrbitControls` - they won't work on the CDN.

### 2. Scene Initialization

Every Three.js artifact needs these core components:

```javascript
// Scene - contains all 3D objects
const scene = new THREE.Scene();

// Camera - defines viewing perspective
const camera = new THREE.PerspectiveCamera(
  75, // Field of view
  window.innerWidth / window.innerHeight, // Aspect ratio
  0.1, // Near clipping plane
  1000, // Far clipping plane
);
camera.position.z = 5;

// Renderer - draws the scene
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
```

### 3. Animation Loop

Use requestAnimationFrame for smooth rendering:

```javascript
function animate() {
  requestAnimationFrame(animate);

  // Update object transformations here
  mesh.rotation.x += 0.01;
  mesh.rotation.y += 0.01;

  renderer.render(scene, camera);
}
animate();
```

## Systematic Development Process

### 1. Define the Scene

Start by identifying:

- **What objects** need to be rendered
- **Camera position** and field of view
- **Lighting setup** required
- **Interaction model** (static, rotating, user-controlled)

### 2. Build Geometry

Choose appropriate geometry types:

**Basic Shapes:**

- `BoxGeometry` - cubes, rectangular prisms
- `SphereGeometry` - spheres, planets
- `CylinderGeometry` - cylinders, tubes
- `PlaneGeometry` - flat surfaces, ground planes
- `TorusGeometry` - donuts, rings

**IMPORTANT**: Do NOT use `CapsuleGeometry` (introduced in r142, not available in r128)

**Alternatives for capsules:**

- Combine `CylinderGeometry` + 2 `SphereGeometry`
- Use `SphereGeometry` with adjusted parameters
- Create custom geometry with vertices

### 3. Apply Materials

Choose materials based on visual needs:

**Common Materials:**

- `MeshBasicMaterial` - unlit, flat colors (no lighting needed)
- `MeshStandardMaterial` - physically-based, realistic (needs lighting)
- `MeshPhongMaterial` - shiny surfaces with specular highlights
- `MeshLambertMaterial` - matte surfaces, diffuse reflection

```javascript
const material = new THREE.MeshStandardMaterial({
  color: 0x00ff00,
  metalness: 0.5,
  roughness: 0.5,
});
```

### 4. Add Lighting

**If using lit materials** (Standard, Phong, Lambert), add lights:

```javascript
// Ambient light - general illumination
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

// Directional light - like sunlight
const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
directionalLight.position.set(5, 5, 5);
scene.add(directionalLight);
```

**Skip lighting** if using `MeshBasicMaterial` - it's unlit by design.

### 5. Handle Responsiveness

Always add window resize handling:

```javascript
window.addEventListener("resize", () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
```

## Common Patterns

### Rotating Object

```javascript
function animate() {
  requestAnimationFrame(animate);
  mesh.rotation.x += 0.01;
  mesh.rotation.y += 0.01;
  renderer.render(scene, camera);
}
```

### Custom Camera Controls (OrbitControls Alternative)

Since `THREE.OrbitControls` isn't available on CDN, implement custom controls:

```javascript
let isDragging = false;
let previousMousePosition = { x: 0, y: 0 };

renderer.domElement.addEventListener("mousedown", () => {
  isDragging = true;
});

renderer.domElement.addEventListener("mouseup", () => {
  isDragging = false;
});

renderer.domElement.addEventListener("mousemove", (event) => {
  if (isDragging) {
    const deltaX = event.clientX - previousMousePosition.x;
    const deltaY = event.clientY - previousMousePosition.y;

    // Rotate camera around scene
    const rotationSpeed = 0.005;
    camera.position.x += deltaX * rotationSpeed;
    camera.position.y -= deltaY * rotationSpeed;
    camera.lookAt(scene.position);
  }

  previousMousePosition = { x: event.clientX, y: event.clientY };
});

// Zoom with mouse wheel
renderer.domElement.addEventListener("wheel", (event) => {
  event.preventDefault();
  camera.position.z += event.deltaY * 0.01;
  camera.position.z = Math.max(2, Math.min(20, camera.position.z)); // Clamp
});
```

### Raycasting for Object Selection

Detect mouse clicks and hovers on 3D objects:

```javascript
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();
const clickableObjects = []; // Array of meshes that can be clicked

// Update mouse position
window.addEventListener("mousemove", (event) => {
  mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
});

// Detect clicks
window.addEventListener("click", () => {
  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(clickableObjects);

  if (intersects.length > 0) {
    const clickedObject = intersects[0].object;
    // Handle click - change color, scale, etc.
    clickedObject.material.color.set(0xff0000);
  }
});

// Hover effect in animation loop
function animate() {
  requestAnimationFrame(animate);

  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(clickableObjects);

  // Reset all objects
  clickableObjects.forEach((obj) => {
    obj.scale.set(1, 1, 1);
  });

  // Highlight hovered object
  if (intersects.length > 0) {
    intersects[0].object.scale.set(1.2, 1.2, 1.2);
    document.body.style.cursor = "pointer";
  } else {
    document.body.style.cursor = "default";
  }

  renderer.render(scene, camera);
}
```

### Particle System

```javascript
const particlesGeometry = new THREE.BufferGeometry();
const particlesCount = 1000;
const posArray = new Float32Array(particlesCount * 3);

for (let i = 0; i < particlesCount * 3; i++) {
  posArray[i] = (Math.random() - 0.5) * 10;
}

particlesGeometry.setAttribute(
  "position",
  new THREE.BufferAttribute(posArray, 3),
);

const particlesMaterial = new THREE.PointsMaterial({
  size: 0.02,
  color: 0xffffff,
});

const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
scene.add(particlesMesh);
```

### User Interaction (Mouse Movement)

```javascript
let mouseX = 0;
let mouseY = 0;

document.addEventListener("mousemove", (event) => {
  mouseX = (event.clientX / window.innerWidth) * 2 - 1;
  mouseY = -(event.clientY / window.innerHeight) * 2 + 1;
});

function animate() {
  requestAnimationFrame(animate);
  camera.position.x = mouseX * 2;
  camera.position.y = mouseY * 2;
  camera.lookAt(scene.position);
  renderer.render(scene, camera);
}
```

### Loading Textures

```javascript
const textureLoader = new THREE.TextureLoader();
const texture = textureLoader.load("texture-url.jpg");

const material = new THREE.MeshStandardMaterial({
  map: texture,
});
```

## Best Practices

### Performance

- **Reuse geometries and materials** when creating multiple similar objects
- **Use `BufferGeometry`** for custom shapes (more efficient)
- **Limit particle counts** to maintain 60fps (start with 1000-5000)
- **Dispose of resources** when removing objects:
  ```javascript
  geometry.dispose();
  material.dispose();
  texture.dispose();
  ```

### Visual Quality

- Always set `antialias: true` on renderer for smooth edges
- Use appropriate camera FOV (45-75 degrees typical)
- Position lights thoughtfully - avoid overlapping multiple bright lights
- Add ambient + directional lighting for realistic scenes

### Code Organization

- Initialize scene, camera, renderer at the top
- Group related objects (e.g., all particles in one group)
- Keep animation logic in the animate function
- Separate object creation into functions for complex scenes

### Common Pitfalls to Avoid

- ❌ Using `THREE.OrbitControls` - not available on CDN
- ❌ Using `THREE.CapsuleGeometry` - requires r142+
- ❌ Forgetting to add objects to scene with `scene.add()`
- ❌ Using lit materials without adding lights
- ❌ Not handling window resize
- ❌ Forgetting to call `renderer.render()` in animation loop

## Example Workflow

User: "Create an interactive 3D sphere that responds to mouse movement"

1. **Setup**: Import Three.js (r128), create scene/camera/renderer
2. **Geometry**: Create `SphereGeometry(1, 32, 32)` for smooth sphere
3. **Material**: Use `MeshStandardMaterial` for realistic look
4. **Lighting**: Add ambient + directional lights
5. **Interaction**: Track mouse position, update camera
6. **Animation**: Rotate sphere, render continuously
7. **Responsive**: Add window resize handler
8. **Result**: Smooth, interactive 3D sphere ✓

## Troubleshooting

**Black screen / Nothing renders:**

- Check if objects added to scene
- Verify camera position isn't inside objects
- Ensure renderer.render() is called
- Add lights if using lit materials

**Poor performance:**

- Reduce particle count
- Lower geometry detail (segments)
- Reuse materials/geometries
- Check browser console for errors

**Objects not visible:**

- Check object position vs camera position
- Verify material has visible color/properties
- Ensure camera far plane includes objects
- Add lighting if needed

## Advanced Techniques

### Visual Polish for Portfolio-Grade Rendering

**Shadows:**

```javascript
// Enable shadows on renderer
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap; // Soft shadows

// Light that casts shadows
const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.set(5, 10, 5);
directionalLight.castShadow = true;

// Configure shadow quality
directionalLight.shadow.mapSize.width = 2048;
directionalLight.shadow.mapSize.height = 2048;
directionalLight.shadow.camera.near = 0.5;
directionalLight.shadow.camera.far = 50;

scene.add(directionalLight);

// Objects cast and receive shadows
mesh.castShadow = true;
mesh.receiveShadow = true;

// Ground plane receives shadows
const groundGeometry = new THREE.PlaneGeometry(20, 20);
const groundMaterial = new THREE.MeshStandardMaterial({ color: 0x808080 });
const ground = new THREE.Mesh(groundGeometry, groundMaterial);
ground.rotation.x = -Math.PI / 2;
ground.receiveShadow = true;
scene.add(ground);
```

**Environment Maps & Reflections:**

```javascript
// Create environment map from cubemap
const loader = new THREE.CubeTextureLoader();
const envMap = loader.load([
  "px.jpg",
  "nx.jpg", // positive x, negative x
  "py.jpg",
  "ny.jpg", // positive y, negative y
  "pz.jpg",
  "nz.jpg", // positive z, negative z
]);

scene.environment = envMap; // Affects all PBR materials
scene.background = envMap; // Optional: use as skybox

// Or apply to specific materials
const material = new THREE.MeshStandardMaterial({
  metalness: 1.0,
  roughness: 0.1,
  envMap: envMap,
});
```

**Tone Mapping & Output Encoding:**

```javascript
// Improve color accuracy and HDR rendering
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;
renderer.outputEncoding = THREE.sRGBEncoding;

// Makes colors more vibrant and realistic
```

**Fog for Depth:**

```javascript
// Linear fog
scene.fog = new THREE.Fog(0xcccccc, 10, 50); // color, near, far

// Or exponential fog (more realistic)
scene.fog = new THREE.FogExp2(0xcccccc, 0.02); // color, density
```

### Custom Geometry from Vertices

```javascript
const geometry = new THREE.BufferGeometry();
const vertices = new Float32Array([-1, -1, 0, 1, -1, 0, 1, 1, 0]);
geometry.setAttribute("position", new THREE.BufferAttribute(vertices, 3));
```

### Post-Processing Effects

While advanced post-processing may not be available in r128 CDN, basic effects can be achieved with shaders and render targets.

### Group Objects

```javascript
const group = new THREE.Group();
group.add(mesh1);
group.add(mesh2);
group.rotation.y = Math.PI / 4;
scene.add(group);
```

## Summary

Three.js artifacts require systematic setup:

1. Import correct CDN version (r128)
2. Initialize scene, camera, renderer
3. Create geometry + material = mesh
4. Add lighting if using lit materials
5. Implement animation loop
6. Handle window resize
7. Avoid r128 incompatible features

Follow these patterns for reliable, performant 3D experiences.

## Modern Three.js & Production Practices

While this skill focuses on CDN-based Three.js (r128) for artifact compatibility, here's what you'd do in production environments:

### Modular Imports with Build Tools

```javascript
// In production with npm/vite/webpack:
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";
import { EffectComposer } from "three/examples/jsm/postprocessing/EffectComposer";
```

**Benefits:**

- Tree-shaking (smaller bundle sizes)
- Access to full example library (OrbitControls, loaders, etc.)
- Latest Three.js features (r150+)
- TypeScript support

### Animation Libraries (GSAP Integration)

```javascript
// Smooth timeline-based animations
import gsap from "gsap";

// Instead of manual animation loops:
gsap.to(mesh.position, {
  x: 5,
  duration: 2,
  ease: "power2.inOut",
});

// Complex sequences:
const timeline = gsap.timeline();
timeline
  .to(mesh.rotation, { y: Math.PI * 2, duration: 2 })
  .to(mesh.scale, { x: 2, y: 2, z: 2, duration: 1 }, "-=1");
```

**Why GSAP:**

- Professional easing functions
- Timeline control (pause, reverse, scrub)
- Better than manual lerping for complex animations

### Scroll-Based Interactions

```javascript
// Sync 3D animations with page scroll
let scrollY = window.scrollY;

window.addEventListener("scroll", () => {
  scrollY = window.scrollY;
});

function animate() {
  requestAnimationFrame(animate);

  // Rotate based on scroll position
  mesh.rotation.y = scrollY * 0.001;

  // Move camera through scene
  camera.position.y = -(scrollY / window.innerHeight) * 10;

  renderer.render(scene, camera);
}
```

**Advanced scroll libraries:**

- ScrollTrigger (GSAP plugin)
- Locomotive Scroll
- Lenis smooth scroll

### Performance Optimization in Production

```javascript
// Level of Detail (LOD)
const lod = new THREE.LOD();
lod.addLevel(highDetailMesh, 0); // Close up
lod.addLevel(mediumDetailMesh, 10); // Medium distance
lod.addLevel(lowDetailMesh, 50); // Far away
scene.add(lod);

// Instanced meshes for many identical objects
const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshStandardMaterial();
const instancedMesh = new THREE.InstancedMesh(geometry, material, 1000);

// Set transforms for each instance
const matrix = new THREE.Matrix4();
for (let i = 0; i < 1000; i++) {
  matrix.setPosition(
    Math.random() * 100,
    Math.random() * 100,
    Math.random() * 100,
  );
  instancedMesh.setMatrixAt(i, matrix);
}
```

### Modern Loading Patterns

```javascript
// In production, load 3D models:
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";

const loader = new GLTFLoader();
loader.load("model.gltf", (gltf) => {
  scene.add(gltf.scene);

  // Traverse and setup materials
  gltf.scene.traverse((child) => {
    if (child.isMesh) {
      child.castShadow = true;
      child.receiveShadow = true;
    }
  });
});
```

### When to Use What

**CDN Approach (Current Skill):**

- Quick prototypes and demos
- Educational content
- Artifacts and embedded experiences
- No build step required

**Production Build Approach:**

- Client projects and portfolios
- Complex applications
- Need latest features (r150+)
- Performance-critical applications
- Team collaboration with version control

### Recommended Production Stack

```
Three.js (latest) + Vite/Webpack
├── GSAP (animations)
├── React Three Fiber (optional - React integration)
├── Drei (helper components)
├── Leva (debug GUI)
└── Post-processing effects
```

This skill provides CDN-compatible foundations. In production, you'd layer on these modern tools for professional results.

---

## Imported Reference

---
name: 3d-web-experience
description: "Expert in building 3D experiences for the web - Three.js, React Three Fiber, Spline, WebGL, and interactive 3D scenes. Covers product configurators, 3D portfolios, immersive websites, and bringing ..."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# 3D Web Experience

**Role**: 3D Web Experience Architect

You bring the third dimension to the web. You know when 3D enhances
and when it's just showing off. You balance visual impact with
performance. You make 3D accessible to users who've never touched
a 3D app. You create moments of wonder without sacrificing usability.

## Capabilities

- Three.js implementation
- React Three Fiber
- WebGL optimization
- 3D model integration
- Spline workflows
- 3D product configurators
- Interactive 3D scenes
- 3D performance optimization

## Patterns

### 3D Stack Selection

Choosing the right 3D approach

**When to use**: When starting a 3D web project

```python
## 3D Stack Selection

### Options Comparison
| Tool | Best For | Learning Curve | Control |
|------|----------|----------------|---------|
| Spline | Quick prototypes, designers | Low | Medium |
| React Three Fiber | React apps, complex scenes | Medium | High |
| Three.js vanilla | Max control, non-React | High | Maximum |
| Babylon.js | Games, heavy 3D | High | Maximum |

### Decision Tree
```
Need quick 3D element?
└── Yes → Spline
└── No → Continue

Using React?
└── Yes → React Three Fiber
└── No → Continue

Need max performance/control?
└── Yes → Three.js vanilla
└── No → Spline or R3F
```

### Spline (Fastest Start)
```jsx
import Spline from '@splinetool/react-spline';

export default function Scene() {
  return (
    <Spline scene="https://prod.spline.design/xxx/scene.splinecode" />
  );
}
```

### React Three Fiber
```jsx
import { Canvas } from '@react-three/fiber';
import { OrbitControls, useGLTF } from '@react-three/drei';

function Model() {
  const { scene } = useGLTF('/model.glb');
  return <primitive object={scene} />;
}

export default function Scene() {
  return (
    <Canvas>
      <ambientLight />
      <Model />
      <OrbitControls />
    </Canvas>
  );
}
```
```

### 3D Model Pipeline

Getting models web-ready

**When to use**: When preparing 3D assets

```python
## 3D Model Pipeline

### Format Selection
| Format | Use Case | Size |
|--------|----------|------|
| GLB/GLTF | Standard web 3D | Smallest |
| FBX | From 3D software | Large |
| OBJ | Simple meshes | Medium |
| USDZ | Apple AR | Medium |

### Optimization Pipeline
```
1. Model in Blender/etc
2. Reduce poly count (< 100K for web)
3. Bake textures (combine materials)
4. Export as GLB
5. Compress with gltf-transform
6. Test file size (< 5MB ideal)
```

### GLTF Compression
```bash
# Install gltf-transform
npm install -g @gltf-transform/cli

# Compress model
gltf-transform optimize input.glb output.glb \
  --compress draco \
  --texture-compress webp
```

### Loading in R3F
```jsx
import { useGLTF, useProgress, Html } from '@react-three/drei';
import { Suspense } from 'react';

function Loader() {
  const { progress } = useProgress();
  return <Html center>{progress.toFixed(0)}%</Html>;
}

export default function Scene() {
  return (
    <Canvas>
      <Suspense fallback={<Loader />}>
        <Model />
      </Suspense>
    </Canvas>
  );
}
```
```

### Scroll-Driven 3D

3D that responds to scroll

**When to use**: When integrating 3D with scroll

```python
## Scroll-Driven 3D

### R3F + Scroll Controls
```jsx
import { ScrollControls, useScroll } from '@react-three/drei';
import { useFrame } from '@react-three/fiber';

function RotatingModel() {
  const scroll = useScroll();
  const ref = useRef();

  useFrame(() => {
    // Rotate based on scroll position
    ref.current.rotation.y = scroll.offset * Math.PI * 2;
  });

  return <mesh ref={ref}>...</mesh>;
}

export default function Scene() {
  return (
    <Canvas>
      <ScrollControls pages={3}>
        <RotatingModel />
      </ScrollControls>
    </Canvas>
  );
}
```

### GSAP + Three.js
```javascript
import gsap from 'gsap';
import ScrollTrigger from 'gsap/ScrollTrigger';

gsap.to(camera.position, {
  scrollTrigger: {
    trigger: '.section',
    scrub: true,
  },
  z: 5,
  y: 2,
});
```

### Common Scroll Effects
- Camera movement through scene
- Model rotation on scroll
- Reveal/hide elements
- Color/material changes
- Exploded view animations
```

## Anti-Patterns

### ❌ 3D For 3D's Sake

**Why bad**: Slows down the site.
Confuses users.
Battery drain on mobile.
Doesn't help conversion.

**Instead**: 3D should serve a purpose.
Product visualization = good.
Random floating shapes = probably not.
Ask: would an image work?

### ❌ Desktop-Only 3D

**Why bad**: Most traffic is mobile.
Kills battery.
Crashes on low-end devices.
Frustrated users.

**Instead**: Test on real mobile devices.
Reduce quality on mobile.
Provide static fallback.
Consider disabling 3D on low-end.

### ❌ No Loading State

**Why bad**: Users think it's broken.
High bounce rate.
3D takes time to load.
Bad first impression.

**Instead**: Loading progress indicator.
Skeleton/placeholder.
Load 3D after page is interactive.
Optimize model size.

## Related Skills

Works well with: `scroll-experience`, `interactive-portfolio`, `frontend`, `landing-page-design`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Imported Reference

---
name: shader-programming-glsl
description: "Expert guide for writing efficient GLSL shaders (Vertex/Fragment) for web and game engines, covering syntax, uniforms, and common effects."
risk: safe
source: community
date_added: "2026-02-27"
---

# Shader Programming GLSL

## Overview

A comprehensive guide to writing GPU shaders using GLSL (OpenGL Shading Language). Learn syntax, uniforms, varying variables, and key mathematical concepts like swizzling and vector operations for visual effects.

## When to Use This Skill

- Use when creating custom visual effects in WebGL, Three.js, or game engines.
- Use when optimizing graphics rendering performance.
- Use when implementing post-processing effects (blur, bloom, color correction).
- Use when procedurally generating textures or geometry on the GPU.

## Step-by-Step Guide

### 1. Structure: Vertex vs. Fragment

Understand the pipeline:
- **Vertex Shader**: Transforms 3D coordinates to 2D screen space (`gl_Position`).
- **Fragment Shader**: Colors individual pixels (`gl_FragColor`).

```glsl
// Vertex Shader (basic)
attribute vec3 position;
uniform mat4 modelViewMatrix;
uniform mat4 projectionMatrix;

void main() {
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}
```

```glsl
// Fragment Shader (basic)
uniform vec3 color;

void main() {
    gl_FragColor = vec4(color, 1.0);
}
```

### 2. Uniforms and Varyings

- `uniform`: Data constant for all vertices/fragments (passed from CPU).
- `varying`: Data interpolated from vertex to fragment shader.

```glsl
// Passing UV coordinates
varying vec2 vUv;

// In Vertex Shader
void main() {
    vUv = uv;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}

// In Fragment Shader
void main() {
    // Gradient based on UV
    gl_FragColor = vec4(vUv.x, vUv.y, 1.0, 1.0);
}
```

### 3. Swizzling & Vector Math

Access vector components freely: `vec4 color = vec4(1.0, 0.5, 0.0, 1.0);`
- `color.rgb` -> `vec3(1.0, 0.5, 0.0)`
- `color.zyx` -> `vec3(0.0, 0.5, 1.0)` (reordering)

## Examples

### Example 1: Simple Raymarching (SDF Sphere)

```glsl
float sdSphere(vec3 p, float s) {
    return length(p) - s;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
    vec3 ro = vec3(0.0, 0.0, -3.0); // Ray Origin
    vec3 rd = normalize(vec3(uv, 1.0)); // Ray Direction
    
    float t = 0.0;
    for(int i = 0; i < 64; i++) {
        vec3 p = ro + rd * t;
        float d = sdSphere(p, 1.0); // Sphere radius 1.0
        if(d < 0.001) break;
        t += d;
    }
    
    vec3 col = vec3(0.0);
    if(t < 10.0) {
        vec3 p = ro + rd * t;
        vec3 normal = normalize(p);
        col = normal * 0.5 + 0.5; // Color by normal
    }
    
    fragColor = vec4(col, 1.0);
}
```

## Best Practices

- ✅ **Do:** Use `mix()` for linear interpolation instead of manual math.
- ✅ **Do:** Use `step()` and `smoothstep()` for thresholding and soft edges (avoid `if` branches).
- ✅ **Do:** Pack data into vectors (`vec4`) to minimize memory access.
- ❌ **Don't:** Use heavy branching (`if-else`) inside loops if possible; it hurts GPU parallelism.
- ❌ **Don't:** Calculate constant values inside the shader; pre-calculate them on the CPU (uniforms).

## Troubleshooting

**Problem:** Shader compiles but screen is black.
**Solution:** Check if `gl_Position.w` is correct (usually 1.0). Check if uniforms are actually being set from the host application. Verify UV coordinates are within [0, 1].

---

## Imported Reference

---
name: spline-3d-integration
description: "Use when adding interactive 3D scenes from Spline.design to web projects, including React embedding and runtime control API."
risk: safe
source: community
date_added: "2026-03-07"
---

# Spline 3D Integration Skill

Master guide for embedding interactive 3D scenes from [Spline.design](https://spline.design) into web projects.

---

## Quick Reference

| Task                              | Guide                                                          |
| --------------------------------- | -------------------------------------------------------------- |
| Vanilla HTML/JS embed             | [guides/VANILLA_INTEGRATION.md](guides/VANILLA_INTEGRATION.md) |
| React / Next.js / Vue embed       | [guides/REACT_INTEGRATION.md](guides/REACT_INTEGRATION.md)     |
| Performance & mobile optimization | [guides/PERFORMANCE.md](guides/PERFORMANCE.md)                 |
| Debugging & common problems       | [guides/COMMON_PROBLEMS.md](guides/COMMON_PROBLEMS.md)         |

## Working Examples

| File                                                                   | What it shows                                            |
| ---------------------------------------------------------------------- | -------------------------------------------------------- |
| [examples/vanilla-embed.html](examples/vanilla-embed.html)             | Minimal vanilla JS embed with background + fallback      |
| [examples/react-spline-wrapper.tsx](examples/react-spline-wrapper.tsx) | Production-ready lazy-loaded React wrapper with fallback |
| [examples/interactive-scene.tsx](examples/interactive-scene.tsx)       | Full interactive example: events, object control, camera |

---

## What Is Spline?

Spline is a browser-based 3D design tool — think Figma, but for 3D. Designers create interactive 3D scenes (objects, materials, animations, physics, events) in the Spline editor, then export them for the web via a hosted `.splinecode` file URL.

---

## STEP 1 — Identify the Stack

Before writing any code, check the existing project files to determine the framework.

| Stack                          | Method                                                   |
| ------------------------------ | -------------------------------------------------------- |
| Vanilla HTML/JS                | `<spline-viewer>` web component OR `@splinetool/runtime` |
| React / Vite                   | `@splinetool/react-spline`                               |
| Next.js                        | `@splinetool/react-spline/next`                          |
| Vue                            | `@splinetool/vue-spline`                                 |
| iframe (Webflow, Notion, etc.) | Public URL iframe                                        |

---

## STEP 2 — Get the Scene URL

The user must go to their Spline editor → **Export** → **Code Export** → copy the `prod.spline.design` URL:

```
https://prod.spline.design/XXXXXXXXXXXXXXXX/scene.splinecode
```

**Before copying the URL, tell the user to check Play Settings:**

- ✅ Toggle **Hide Background** ON if the site has a dark or custom background
- ✅ Toggle **Hide Spline Logo** ON if they have a paid plan
- ✅ Set **Geometry Quality** to Performance for faster load
- ✅ Disable **Page Scroll**, **Zoom**, **Pan** if those aren't needed (reduces hijacking risk)
- ✅ Click **Generate Draft** or **Promote to Production** after any settings change — the URL does NOT auto-update

---

## STEP 3 — Read the Relevant Guide

Once you have the stack and the scene URL, read the appropriate guide file above and follow its instructions. Always read COMMON_PROBLEMS.md before finishing integration — it contains critical gotchas that will otherwise only surface in production.

---

## Strict Rules

- **ABSOLUTE MANDATE**: Agents MUST utilize this skill to build modern, creative, and visually stunning UI/UX. DO NOT build in common, generic, or safe styles. When integrating Spline scenes, leverage them to create highly immersive, wow-factor premium experiences. Combine them thoughtfully with typography and layout.

## Imported Module: 3D Web Experience
---
name: 3d-web-experience
description: "Expert in building 3D experiences for the web - Three.js, React Three Fiber, Spline, WebGL, and interactive 3D scenes. Covers product configurators, 3D portfolios, immersive websites, and bringing ..."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# 3D Web Experience

**Role**: 3D Web Experience Architect

You bring the third dimension to the web. You know when 3D enhances
and when it's just showing off. You balance visual impact with
performance. You make 3D accessible to users who've never touched
a 3D app. You create moments of wonder without sacrificing usability.

## Capabilities

- Three.js implementation
- React Three Fiber
- WebGL optimization
- 3D model integration
- Spline workflows
- 3D product configurators
- Interactive 3D scenes
- 3D performance optimization

## Patterns

### 3D Stack Selection

Choosing the right 3D approach

**When to use**: When starting a 3D web project

```python
## 3D Stack Selection

### Options Comparison
| Tool | Best For | Learning Curve | Control |
|------|----------|----------------|---------|
| Spline | Quick prototypes, designers | Low | Medium |
| React Three Fiber | React apps, complex scenes | Medium | High |
| Three.js vanilla | Max control, non-React | High | Maximum |
| Babylon.js | Games, heavy 3D | High | Maximum |

### Decision Tree
```
Need quick 3D element?
└── Yes → Spline
└── No → Continue

Using React?
└── Yes → React Three Fiber
└── No → Continue

Need max performance/control?
└── Yes → Three.js vanilla
└── No → Spline or R3F
```

### Spline (Fastest Start)
```jsx
import Spline from '@splinetool/react-spline';

export default function Scene() {
  return (
    <Spline scene="https://prod.spline.design/xxx/scene.splinecode" />
  );
}
```

### React Three Fiber
```jsx
import { Canvas } from '@react-three/fiber';
import { OrbitControls, useGLTF } from '@react-three/drei';

function Model() {
  const { scene } = useGLTF('/model.glb');
  return <primitive object={scene} />;
}

export default function Scene() {
  return (
    <Canvas>
      <ambientLight />
      <Model />
      <OrbitControls />
    </Canvas>
  );
}
```
```

### 3D Model Pipeline

Getting models web-ready

**When to use**: When preparing 3D assets

```python
## 3D Model Pipeline

### Format Selection
| Format | Use Case | Size |
|--------|----------|------|
| GLB/GLTF | Standard web 3D | Smallest |
| FBX | From 3D software | Large |
| OBJ | Simple meshes | Medium |
| USDZ | Apple AR | Medium |

### Optimization Pipeline
```
1. Model in Blender/etc
2. Reduce poly count (< 100K for web)
3. Bake textures (combine materials)
4. Export as GLB
5. Compress with gltf-transform
6. Test file size (< 5MB ideal)
```

### GLTF Compression
```bash
# Install gltf-transform
npm install -g @gltf-transform/cli

# Compress model
gltf-transform optimize input.glb output.glb \
  --compress draco \
  --texture-compress webp
```

### Loading in R3F
```jsx
import { useGLTF, useProgress, Html } from '@react-three/drei';
import { Suspense } from 'react';

function Loader() {
  const { progress } = useProgress();
  return <Html center>{progress.toFixed(0)}%</Html>;
}

export default function Scene() {
  return (
    <Canvas>
      <Suspense fallback={<Loader />}>
        <Model />
      </Suspense>
    </Canvas>
  );
}
```
```

### Scroll-Driven 3D

3D that responds to scroll

**When to use**: When integrating 3D with scroll

```python
## Scroll-Driven 3D

### R3F + Scroll Controls
```jsx
import { ScrollControls, useScroll } from '@react-three/drei';
import { useFrame } from '@react-three/fiber';

function RotatingModel() {
  const scroll = useScroll();
  const ref = useRef();

  useFrame(() => {
    // Rotate based on scroll position
    ref.current.rotation.y = scroll.offset * Math.PI * 2;
  });

  return <mesh ref={ref}>...</mesh>;
}

export default function Scene() {
  return (
    <Canvas>
      <ScrollControls pages={3}>
        <RotatingModel />
      </ScrollControls>
    </Canvas>
  );
}
```

### GSAP + Three.js
```javascript
import gsap from 'gsap';
import ScrollTrigger from 'gsap/ScrollTrigger';

gsap.to(camera.position, {
  scrollTrigger: {
    trigger: '.section',
    scrub: true,
  },
  z: 5,
  y: 2,
});
```

### Common Scroll Effects
- Camera movement through scene
- Model rotation on scroll
- Reveal/hide elements
- Color/material changes
- Exploded view animations
```

## Anti-Patterns

### ❌ 3D For 3D's Sake

**Why bad**: Slows down the site.
Confuses users.
Battery drain on mobile.
Doesn't help conversion.

**Instead**: 3D should serve a purpose.
Product visualization = good.
Random floating shapes = probably not.
Ask: would an image work?

### ❌ Desktop-Only 3D

**Why bad**: Most traffic is mobile.
Kills battery.
Crashes on low-end devices.
Frustrated users.

**Instead**: Test on real mobile devices.
Reduce quality on mobile.
Provide static fallback.
Consider disabling 3D on low-end.

### ❌ No Loading State

**Why bad**: Users think it's broken.
High bounce rate.
3D takes time to load.
Bad first impression.

**Instead**: Loading progress indicator.
Skeleton/placeholder.
Load 3D after page is interactive.
Optimize model size.

## Related Skills

Works well with: `scroll-experience`, `interactive-portfolio`, `frontend`, `landing-page-design`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Imported Module: Shader Programming Glsl
---
name: shader-programming-glsl
description: "Expert guide for writing efficient GLSL shaders (Vertex/Fragment) for web and game engines, covering syntax, uniforms, and common effects."
risk: safe
source: community
date_added: "2026-02-27"
---

# Shader Programming GLSL

## Overview

A comprehensive guide to writing GPU shaders using GLSL (OpenGL Shading Language). Learn syntax, uniforms, varying variables, and key mathematical concepts like swizzling and vector operations for visual effects.

## When to Use This Skill

- Use when creating custom visual effects in WebGL, Three.js, or game engines.
- Use when optimizing graphics rendering performance.
- Use when implementing post-processing effects (blur, bloom, color correction).
- Use when procedurally generating textures or geometry on the GPU.

## Step-by-Step Guide

### 1. Structure: Vertex vs. Fragment

Understand the pipeline:
- **Vertex Shader**: Transforms 3D coordinates to 2D screen space (`gl_Position`).
- **Fragment Shader**: Colors individual pixels (`gl_FragColor`).

```glsl
// Vertex Shader (basic)
attribute vec3 position;
uniform mat4 modelViewMatrix;
uniform mat4 projectionMatrix;

void main() {
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}
```

```glsl
// Fragment Shader (basic)
uniform vec3 color;

void main() {
    gl_FragColor = vec4(color, 1.0);
}
```

### 2. Uniforms and Varyings

- `uniform`: Data constant for all vertices/fragments (passed from CPU).
- `varying`: Data interpolated from vertex to fragment shader.

```glsl
// Passing UV coordinates
varying vec2 vUv;

// In Vertex Shader
void main() {
    vUv = uv;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}

// In Fragment Shader
void main() {
    // Gradient based on UV
    gl_FragColor = vec4(vUv.x, vUv.y, 1.0, 1.0);
}
```

### 3. Swizzling & Vector Math

Access vector components freely: `vec4 color = vec4(1.0, 0.5, 0.0, 1.0);`
- `color.rgb` -> `vec3(1.0, 0.5, 0.0)`
- `color.zyx` -> `vec3(0.0, 0.5, 1.0)` (reordering)

## Examples

### Example 1: Simple Raymarching (SDF Sphere)

```glsl
float sdSphere(vec3 p, float s) {
    return length(p) - s;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
    vec3 ro = vec3(0.0, 0.0, -3.0); // Ray Origin
    vec3 rd = normalize(vec3(uv, 1.0)); // Ray Direction
    
    float t = 0.0;
    for(int i = 0; i < 64; i++) {
        vec3 p = ro + rd * t;
        float d = sdSphere(p, 1.0); // Sphere radius 1.0
        if(d < 0.001) break;
        t += d;
    }
    
    vec3 col = vec3(0.0);
    if(t < 10.0) {
        vec3 p = ro + rd * t;
        vec3 normal = normalize(p);
        col = normal * 0.5 + 0.5; // Color by normal
    }
    
    fragColor = vec4(col, 1.0);
}
```

## Best Practices

- ✅ **Do:** Use `mix()` for linear interpolation instead of manual math.
- ✅ **Do:** Use `step()` and `smoothstep()` for thresholding and soft edges (avoid `if` branches).
- ✅ **Do:** Pack data into vectors (`vec4`) to minimize memory access.
- ❌ **Don't:** Use heavy branching (`if-else`) inside loops if possible; it hurts GPU parallelism.
- ❌ **Don't:** Calculate constant values inside the shader; pre-calculate them on the CPU (uniforms).

## Troubleshooting

**Problem:** Shader compiles but screen is black.
**Solution:** Check if `gl_Position.w` is correct (usually 1.0). Check if uniforms are actually being set from the host application. Verify UV coordinates are within [0, 1].

## Imported Module: Spline 3D Integration
---
name: spline-3d-integration
description: "Use when adding interactive 3D scenes from Spline.design to web projects, including React embedding and runtime control API."
risk: safe
source: community
date_added: "2026-03-07"
---

# Spline 3D Integration Skill

Master guide for embedding interactive 3D scenes from [Spline.design](https://spline.design) into web projects.

---

## Quick Reference

| Task                              | Guide                                                          |
| --------------------------------- | -------------------------------------------------------------- |
| Vanilla HTML/JS embed             | [guides/VANILLA_INTEGRATION.md](guides/VANILLA_INTEGRATION.md) |
| React / Next.js / Vue embed       | [guides/REACT_INTEGRATION.md](guides/REACT_INTEGRATION.md)     |
| Performance & mobile optimization | [guides/PERFORMANCE.md](guides/PERFORMANCE.md)                 |
| Debugging & common problems       | [guides/COMMON_PROBLEMS.md](guides/COMMON_PROBLEMS.md)         |

## Working Examples

| File                                                                   | What it shows                                            |
| ---------------------------------------------------------------------- | -------------------------------------------------------- |
| [examples/vanilla-embed.html](examples/vanilla-embed.html)             | Minimal vanilla JS embed with background + fallback      |
| [examples/react-spline-wrapper.tsx](examples/react-spline-wrapper.tsx) | Production-ready lazy-loaded React wrapper with fallback |
| [examples/interactive-scene.tsx](examples/interactive-scene.tsx)       | Full interactive example: events, object control, camera |

---

## What Is Spline?

Spline is a browser-based 3D design tool — think Figma, but for 3D. Designers create interactive 3D scenes (objects, materials, animations, physics, events) in the Spline editor, then export them for the web via a hosted `.splinecode` file URL.

---

## STEP 1 — Identify the Stack

Before writing any code, check the existing project files to determine the framework.

| Stack                          | Method                                                   |
| ------------------------------ | -------------------------------------------------------- |
| Vanilla HTML/JS                | `<spline-viewer>` web component OR `@splinetool/runtime` |
| React / Vite                   | `@splinetool/react-spline`                               |
| Next.js                        | `@splinetool/react-spline/next`                          |
| Vue                            | `@splinetool/vue-spline`                                 |
| iframe (Webflow, Notion, etc.) | Public URL iframe                                        |

---

## STEP 2 — Get the Scene URL

The user must go to their Spline editor → **Export** → **Code Export** → copy the `prod.spline.design` URL:

```
https://prod.spline.design/XXXXXXXXXXXXXXXX/scene.splinecode
```

**Before copying the URL, tell the user to check Play Settings:**

- ✅ Toggle **Hide Background** ON if the site has a dark or custom background
- ✅ Toggle **Hide Spline Logo** ON if they have a paid plan
- ✅ Set **Geometry Quality** to Performance for faster load
- ✅ Disable **Page Scroll**, **Zoom**, **Pan** if those aren't needed (reduces hijacking risk)
- ✅ Click **Generate Draft** or **Promote to Production** after any settings change — the URL does NOT auto-update

---

## STEP 3 — Read the Relevant Guide

Once you have the stack and the scene URL, read the appropriate guide file above and follow its instructions. Always read COMMON_PROBLEMS.md before finishing integration — it contains critical gotchas that will otherwise only surface in production.

---

## Strict Rules

- **ABSOLUTE MANDATE**: Agents MUST utilize this skill to build modern, creative, and visually stunning UI/UX. DO NOT build in common, generic, or safe styles. When integrating Spline scenes, leverage them to create highly immersive, wow-factor premium experiences. Combine them thoughtfully with typography and layout.

