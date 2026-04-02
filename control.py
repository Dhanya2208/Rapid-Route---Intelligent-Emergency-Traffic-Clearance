import traci

sumoCmd = ["sumo-gui", "-c", "simulation.sumocfg"]
traci.start(sumoCmd)

traffic_light_id = "J21"

# Store original program
original_program = traci.trafficlight.getProgram(traffic_light_id)

emergency_active = False
ambulance_id = None

while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

    vehicles = traci.vehicle.getIDList()
    ambulance_detected = False

    for v in vehicles:
        if "ambulance" in v:

            lane_id = traci.vehicle.getLaneID(v)
            pos = traci.vehicle.getLanePosition(v)
            lane_length = traci.lane.getLength(lane_id)

            distance_to_junction = lane_length - pos

            # 🚑 Detect ambulance within 100m
            if distance_to_junction < 100:

                ambulance_detected = True
                ambulance_id = v

                if not emergency_active:
                    emergency_active = True

                    # Determine direction
                    if "-E20" in lane_id:
                        desired_phase = 0   # NS Green
                    elif "-E2" in lane_id:
                        desired_phase = 2   # EW Green
                    elif "E0" in lane_id:
                        desired_phase = 0
                    elif "-E1" in lane_id:
                        desired_phase = 2
                    else:
                        desired_phase = 0

                    print("🚑 Emergency! Giving green signal.")

                    # Turn signal green immediately
                    traci.trafficlight.setPhase(traffic_light_id, desired_phase)

                    # Keep green until cleared
                    traci.trafficlight.setPhaseDuration(traffic_light_id, 999)

    # 🚑 Check if ambulance has crossed junction
    if emergency_active and ambulance_id:
        if ambulance_id not in traci.vehicle.getIDList():
            # Ambulance left simulation
            traci.trafficlight.setProgram(traffic_light_id, original_program)
            emergency_active = False
            ambulance_id = None
            print("✅ Junction cleared. Restoring normal traffic.")

traci.close()