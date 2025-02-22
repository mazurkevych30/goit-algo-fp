def change_color(step, base_color="#1296F5"):
    r, g, b = (
        int(base_color[1:3], 16),
        int(base_color[3:5], 16),
        int(base_color[5:7], 16),
    )

    r_light = min(255, r + step * 10)
    g_light = min(255, g + step * 10)
    b_light = min(255, b + step * 10)

    return f"#{hex(r_light)[2:].zfill(2)}{hex(g_light)[2:].zfill(2)}{hex(b_light)[2:].zfill(2)}"