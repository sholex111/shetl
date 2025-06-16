import os

print("ALL ENV VARS:")
for k, v in os.environ.items():
    print(k, "=", v)