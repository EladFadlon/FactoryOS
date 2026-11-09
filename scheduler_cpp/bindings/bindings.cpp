#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "scheduler.hpp"

namespace py = pybind11;
using namespace factoryos;

PYBIND11_MODULE(factoryos_scheduler, m) {
    m.doc() = "FactoryOS C++ scheduling engine";

    py::class_<Step>(m, "Step")
        .def(py::init<std::string, int>())
        .def_readwrite("machine_type", &Step::machine_type)
        .def_readwrite("minutes", &Step::minutes);

    py::class_<Job>(m, "Job")
        .def(py::init<int, int, int, std::vector<Step>>())
        .def_readwrite("id", &Job::id)
        .def_readwrite("due_minute", &Job::due_minute)
        .def_readwrite("priority", &Job::priority)
        .def_readwrite("route", &Job::route);

    py::class_<Assignment>(m, "Assignment")
        .def_readonly("job_id", &Assignment::job_id)
        .def_readonly("machine_type", &Assignment::machine_type)
        .def_readonly("start_minute", &Assignment::start_minute)
        .def_readonly("end_minute", &Assignment::end_minute);

    m.def("schedule", &schedule, "Build a production schedule for the given jobs");
}
