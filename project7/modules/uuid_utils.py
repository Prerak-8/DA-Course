import uuid

# UUID generation utility function.

def generate_uuid():
    uuid_system = uuid.uuid1()

    print("Generated UUID based on system:", uuid_system)

    uuid_random = uuid.uuid4()

    print("Generated random UUID:", uuid_random)
    print("--------------------------\n")