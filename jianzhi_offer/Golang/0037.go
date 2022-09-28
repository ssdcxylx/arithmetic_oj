package main

func asteroidCollision(asteroids []int) (stack []int) {
    for _, aster := range asteroids {
        alive := true
        for alive && aster < 0 && len(stack) > 0 && stack[len(stack)-1] > 0 {
            alive = stack[len(stack)-1] < -aster
            if stack[len(stack)-1] <= -aster {
                stack = stack[:len(stack)-1]
            }
        }
        if alive {
            stack = append(stack, aster)
        }
    }
    return 
}