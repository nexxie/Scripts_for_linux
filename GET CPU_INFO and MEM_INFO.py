import re

# Get ino from  /proc/meminfo
with open('/proc/meminfo') as mem_info:
    for line in mem_info:
        if line.startswith('MemTotal'):
            memory_total = int(re.findall(r'\d+', line)[0])  # memory in KB
            break

# Get ino from /proc/cpuinfo
with open('/proc/cpuinfo') as cpu_info:
    cpu_cores = 0
    for line in cpu_info:
        if line.startswith('processor'):
            cpu_cores += 1

print(memory_total)
print(cpu_cores)
