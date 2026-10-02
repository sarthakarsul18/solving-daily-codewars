def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_time = shark_distance/(shark_speed*0.5)
        you = pontoon_distance/you_speed
        return "Alive!" if shark_time>you else "Shark Bait!"
    else:
        shark_time = shark_distance/shark_speed
        you = pontoon_distance/you_speed
        return "Alive!" if shark_time>you else "Shark Bait!"