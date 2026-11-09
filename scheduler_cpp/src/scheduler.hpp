#pragma once
#include <string>
#include <vector>

namespace factoryos {

// One processing step of a job on a machine type.
struct Step {
    std::string machine_type;
    int minutes;
};

// A unit of work: one product instance with its route.
struct Job {
    int id;
    int due_minute;
    int priority;            // higher = more urgent
    std::vector<Step> route;
};

// One scheduled operation in the output plan.
struct Assignment {
    int job_id;
    std::string machine_type;
    int start_minute;
    int end_minute;
};

// Phase 5: implement the same algorithm as the Python reference version,
// then prove both return identical schedules for the same input.
std::vector<Assignment> schedule(const std::vector<Job>& jobs);

}  // namespace factoryos
