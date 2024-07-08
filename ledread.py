def read_leds_cfg(file_path):
    with open(file_path, 'r') as file:
        # Skip the comment line
        header = file.readline().strip()

        # Read the next 32 lines
        led_values = []
        for _ in range(32):
            line = file.readline().strip()
            led_value = int(line)
            if 0 <= led_value <= 253:
                led_values.append(led_value)
            else:
                raise ValueError(f"Value {led_value} out of range (0-253)")

    return header, led_values


# Example usage
file_path = 'leds.cfg'
header, led_values = read_leds_cfg(file_path)
print("Header:", header)
print("LED Values:", led_values)
