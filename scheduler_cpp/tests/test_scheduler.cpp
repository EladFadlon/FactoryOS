#include <gtest/gtest.h>
#include "scheduler.hpp"

using namespace factoryos;

TEST(Scheduler, EmptyInputGivesEmptyPlan) {
    EXPECT_TRUE(schedule({}).empty());
}
