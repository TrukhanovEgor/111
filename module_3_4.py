def single_root_world(root_worg, *Other_world):
    some_world = []
    root_worg_lower = root_worg.lower()

    for world in Other_world:
        world_lower = world.lower()

        if root_worg_lower in world_lower or world_lower or world_lower in root_worg_lower:
            some_world.append(world)

    return some_world


result1 = single_root_world('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_world('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
