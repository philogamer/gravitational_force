### GRAVITATIONAL SIMULATION GAME
Gravitational simulation game based on Newton's law (F = GMm/r²). Includes features for generating random map, non-colliding planets and calculating orbits using vectors.
<img width="1749" height="907" alt="image" src="https://github.com/user-attachments/assets/e4144b68-637c-42bc-90c0-21180e333e60" />

## HOW THIS WAS MADE
this project was made with pygame and physics

## play?
-**Control**:  Click, see your object, drag, then release
-**Resetmap**: press P

## rules
- **Drag range is limited** — you can't slingshot infinitely far.
- **You cannot re-aim while the star is flying.** No more fun if can!
- **Press P anytime** to see will next map can satisfy you

## aim?
No winning or losing, just pure chaos. Your goal is to view interesting trajectories by gravity

## planet
Each planet exerts a gravitational pull on the star following Newton's law of universal gravitation:
(F = GMm/r²)
- The **faint outer circle** around each planet visualizes its mass (bigger circle = stronger gravitational force), if you can't see it just because the planet is bigger than the mass very much
- Only planets **currently visible on screen** affect the star.
- If the object touches a planet, it **stops at the planet's edge** and now you can drag it again

## friendly reminder
If the star flies off the edge of the screen, **don't close the game!**, the gravity will take it back for you

## map render
Each map is generated with:
- 9–15 planets with **random** positions, sizes, and masses
- **Non-overlapping planet** algorithm to keep planets from stacking

## science
Simulate **Newtonian orbital mechanics** in real time:
- Gravitational force is calculated using vector math (`pygame.math.Vector2`)
- Velocity is integrated each frame based on the sum of all gravitational forces


## heres how to run the project
1. Choose a release

2. Choose zip or rar

3. Open the exe file

and enjoy

## AI DISCLOSURE
I used it to scale the number of each planet and speed
