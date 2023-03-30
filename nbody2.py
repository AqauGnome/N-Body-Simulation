import pygame, sys, random, math; from operator import add

def main():
    pygame.init()

    # main variables
    winWidth = 1920
    winHeight = 1080

    # simulation variables
    entityCount = 3
    gravityConst = 6.67*10**-11
    entityMass = 10
    timeStep = 1
    # Note: timestep being changed doesnt seem to affect the simulation
    
    # random starting positions not near the borders of window
    xCoordinates = random.sample(range(100, (winWidth - 100)), entityCount)
    yCoordinates = random.sample(range(100, (winHeight - 100)), entityCount)

    # starting velocity list (equal to zero)
    xVelocities = entityCount * [0]
    yVelocities = entityCount * [0]

    # is displacement and velcoity being reset everytime? 
    deltaXDisp, deltaYDisp, deltaXVel, deltaYVel= [0],[0],[0],[0]
    clock = pygame.time.Clock()

    # creating a pygame window 
    window = pygame.display.set_mode((winWidth, winHeight), pygame.FULLSCREEN)
    pygame.display.set_caption("Gravity Simulation Three")

    run = True

    while run:
        # run sim at 60hz
        clock.tick(60)
        # fill window with light colour
        window.fill((224, 225, 221))
        # close program if exited
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # escape key quits game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        deltaXCoordinates = []
        deltaYCoordinates = []
        deltaXVelocities = []
        deltaYVelocities = []
        
        # iterate through list of entities to calculate forces
        for i in range(entityCount):

            pygame.draw.circle(window,(13, 27, 42), (xCoordinates[i], yCoordinates[i]), 6)

            # current positions
            currentXPosition = xCoordinates[i]
            currentYPosition = yCoordinates[i]

            # removing the current position so as to not divide by zero
            xCoordinates.remove(xCoordinates[i])
            yCoordinates.remove(yCoordinates[i])

            # initialising radius variables
            xRadius, yRadius = 0,0
            # iterate through list of other entities to calculate forces
            for n in range(entityCount - 1):
                # finding net radius to use with gravity equation
                xRadius += (xCoordinates[n] - currentXPosition)
                yRadius += (yCoordinates[n] - currentYPosition)
            
            # re-adding current positions
            xCoordinates.insert(i, currentXPosition)
            yCoordinates.insert(i, currentYPosition)
            # finding force applied 
            xForce = (gravityConst*(entityMass**2)/(xRadius**2))/entityMass
            yForce = (gravityConst*(entityMass**2)/(yRadius**2))/entityMass
            # finding delta position
            xDisplacement = (xVelocities[i]*timeStep)+((timeStep**2)/2)*xForce
            yDisplacement = (yVelocities[i]*timeStep)+((timeStep**2)/2)*yForce
            # finding new velocities
            newXVelocity = math.sqrt((xVelocities[i]**2)+(2*xForce*xDisplacement))
            newYVelocity = math.sqrt((yVelocities[i]**2)+(2*yForce*yDisplacement))
            # appending new positions to list
            deltaXCoordinates.append(xDisplacement)
            deltaYCoordinates.append(yDisplacement)
            # new velocities list
            deltaXVelocities.append(newXVelocity)
            deltaYVelocities.append(newYVelocity)
            
        # add change in position
        xCoordinates = list(map(add,xCoordinates,deltaXCoordinates))
        yCoordinates = list(map(add,yCoordinates,deltaYCoordinates))
        # adding velocity
        xVelocities = list(map(add, xVelocities, deltaXVelocities))
        yVelocities = list(map(add, yVelocities, deltaYVelocities))
        print(f"x radius: {xRadius} \ny radius: {yRadius}")
        print(f"x velocities: {xVelocities} \ny Velocities: {yVelocities}")
        pygame.display.update()

    pygame.quit
main()