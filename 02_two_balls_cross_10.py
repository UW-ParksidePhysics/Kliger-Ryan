import vpython as vp

initial_position = vp.vector(-5., -5., -3.)
initial_velocity = vp.vector(5., 5., 3.)
initial_position2 = vp.vector(5., 5., 3)
initial_velocity2 = vp.vector(-5., -5., -3.)
ball = vp.sphere(pos=initial_position, radius=0.5, color=vp.color.red, make_trail=True, trail_type="points", interval=10, retain=50)
ball2 = vp.sphere(pos=initial_position2, radius=0.5, color=vp.color.blue, make_trail=True, trail_type="points", interval=10, retain=50)
animation_time_step = 0.01
rate_of_animation = 1/animation_time_step
time_step = 0.001
stop_time = 15

time = 0.
while time < stop_time:
    vp.rate(rate_of_animation)
    x = initial_position.x + initial_velocity.x * time
    y = initial_position.y + initial_velocity.y * time
    z = initial_position.z + initial_velocity.z * time
    ball.pos = vp.vector(x, y, z)
    time += time_step
    x = initial_position2.x + initial_velocity2.x * time
    y = initial_position2.y + initial_velocity2.y * time
    z = initial_position2.z + initial_velocity2.z * time
    ball2.pos = vp.vector(x, y, z)
    time += time_step