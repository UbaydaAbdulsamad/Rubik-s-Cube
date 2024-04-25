# Rubik's Cube
This small python app demonstrates detecting different color for the same object and explains the reason behind it.
<p align="center">
  <img src="https://github.com/UbaydaAbdulsamad/Rubik-s-Cube/assets/80641961/d24d941b-5a79-44e1-9eef-e494de82aaeb" alt="User Interface">
</p>



# Experiment and observation:
The Rubik’s cube has been photographed in various lighting conditions and view angles, then loaded into the application:

<p align="center">
<img src="https://github.com/UbaydaAbdulsamad/Rubik-s-Cube/assets/80641961/6108fd04-d733-46ea-8e89-63ab54bbc19d"
</p>
  
By detecting the identical colors on the cube in different surfaces and among different images, a color shift has been observed even though the colors are identical.

<p align="center">
<img src="https://github.com/UbaydaAbdulsamad/Rubik-s-Cube/assets/80641961/46cb00fa-816b-4d6b-aad9-2a66c0fe00a0">
</p>

# Explanation:
There are various reasons behind the difference in the colors detected, the following list will diagnose these results and provide a brief explanation:
- **Reflection**:
The light received by the camera represents the fusion of the object's diffuse color and the environment lighting color. By changing the place where the cube is photographed, the surrounding environment will alter the colors reflected.
- **Lighting**:
The amount of voltage each sensor cell in the sensor image generates is related to the intensity of the
light received. Thus, same object will appear to have darker colors in shade than it would in light.
- **Auto exposure**:
The mobile camera has an auto exposure feature so that it can optimize the sensitivity of the image
sensor to adapt with respect to divert lighting conditions. Each image has different shooting
parameters, namely; shutter speed, aperture and iso.
- **Auto white balance**:
The human brain can perceive colors of objects based on the ambient color of the environment; thus,
a white paper exposed to sunlight is perceived as white even though its actual color is yellow. But
the image might be viewed in different atmospheric lighting conditions. The camera fixes this
problem by applying color balance effect to the snapped image which will result in inconsistent color
tone.
