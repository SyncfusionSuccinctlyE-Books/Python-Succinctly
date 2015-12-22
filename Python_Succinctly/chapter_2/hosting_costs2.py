#!/usr/bin/env python3

# The cost of one server per hour.
cost_per_hour = 1.02

# Compute the costs for one server.
cost_per_day = 24 * cost_per_hour
cost_per_month = 30 * cost_per_day

# Compute the costs for twenty servers
cost_per_day_twenty = 20 * cost_per_day
cost_per_month_twenty = 20 * cost_per_month

# Budgeting
budget = 1836
operational_days = budget / cost_per_day

# Display the results.
print('Cost to operate one server per day is ${:.2f}.'.format(cost_per_day))
print('Cost to operate one server per month is ${:.2f}.'.format(cost_per_month))
print('Cost to operate twenty servers per day is ${:.2f}.'.format(cost_per_day_twenty))
print('Cost to operate twenty servers per month is ${:.2f}.'.format(cost_per_month_twenty))
print('A server can operate on a ${0:.2f} budget for {1:.0f} days.'.format(budget, operational_days))
