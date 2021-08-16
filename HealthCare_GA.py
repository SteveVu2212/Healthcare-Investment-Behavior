import math
import numpy as np
import random
import matplotlib.pyplot as plt

class HealthCare:
    def __init__(self, meta_parameters):
        self.population_size = meta_parameters.get("population_size")
        self.num_children = meta_parameters.get("num_children")
        self.num_periods = meta_parameters.get("num_periods")
        self.initial_health = meta_parameters.get("initial_health")
        self.mutate_prob = meta_parameters.get("mutate_prob")

    def Incomes(self, H):
        M = 100; N = 100; W = 10; T = 300; y = 1; v = 1
        total_harvest_area = M*N
        total_dots = T*total_harvest_area/(M*W)
        harvest_rows = max(0,M*(1-y*((100-H)/100)))
        harvest_area = W*harvest_rows
        harvest_point = harvest_area*total_dots/total_harvest_area
        return harvest_point*v

    def HealthRegained(self, health_investment, health_after_harvest):
        k = 0.007
        numerator = math.exp(k*health_investment)
        denominator = numerator + (100-health_after_harvest)/health_after_harvest
        health_regain = 100*(numerator/denominator) - health_after_harvest
        return health_regain

    def LifeEnjoyment(self, life_investment, current_health):
        c = 700
        a = 45
        life_enjoyment = c*(current_health/100)*(life_investment/(life_investment+a))
        return life_enjoyment

    def health_degeneration(self, start_health, fixed_point, current_period):
        degen_slope = 4
        health_losses = fixed_point + current_period * degen_slope
        health_after_harvest = start_health - health_losses
        return health_after_harvest

    def fitness_calculation(self, strategy):
        start_health = self.initial_health
        start_savings = 0

        lst_income = []
        health = []
        fitness = []
        savings = []
        lst_health_investment = []
        lst_life_investment = []

        for i in range(self.num_periods):
            income = self.Incomes(start_health)
            lst_income.append(income)

            health_investment = strategy[0][i]*(start_savings + income)
            lst_health_investment.append(health_investment)

            health_after_harvest = self.health_degeneration(start_health, 15, i+1)
            if health_after_harvest <= 0:
                regained_health = 0
            else:
                regained_health = self.HealthRegained(health_investment, health_after_harvest)
            
            health_after_regained = max(0, health_after_harvest + regained_health)

            if health_after_regained >= 100:
                current_health = 100
            elif 0 < health_after_regained < 100:
                current_health = health_after_regained
            else:
                current_health = 0
            health.append(current_health)

            life_investment = strategy[1][i] * (start_savings + income)
            lst_life_investment.append(life_investment)
            fitness.append(self.LifeEnjoyment(life_investment, current_health))

            savings.append((start_savings + income) * strategy[2][i])

            start_savings = (start_savings + income) * strategy[2][i]

            start_health = current_health

        total_fitness = sum(fitness)

        return total_fitness, health, fitness, savings, lst_health_investment, lst_life_investment, lst_income

    def generate_population(self):
        population = []
        for _ in range(self.population_size):
            health_investment_percent = []
            life_investment_percent = []
            savings_percent = []
            while len(health_investment_percent) < self.num_periods:
                h = random.uniform(0,1)
                l = random.uniform(0,1)
                s = random.uniform(0,1)
                health_investment_percent.append(h / (h + l + s))
                life_investment_percent.append(l / (h + l + s))
                savings_percent.append(s / (h + l + s))
            population.append([health_investment_percent, life_investment_percent, savings_percent])
        return population

    def mutate(self, individual):
        mutate_decrease = [random.uniform(0.9, 1) for _ in range(self.num_periods)]
        mutate_increase = [random.uniform(1, 1.1) for _ in range(self.num_periods)]
        for i in range(self.num_periods):
            if random.random() < self.mutate_prob:
                health_investment_percent = individual[0][i] * mutate_decrease[i]
            else:
                health_investment_percent = individual[0][i] * mutate_increase[i]

            if random.random() < self.mutate_prob:
                life_investment_percent = individual[1][i] * mutate_decrease[i]
            else:
                life_investment_percent = individual[1][i] * mutate_increase[i]
            
            if random.random() < self.mutate_prob:
                savings_percent = individual[2][i] * mutate_decrease[i]
            else:
                savings_percent = individual[2][i] * mutate_increase[i]

            total_values = health_investment_percent + life_investment_percent + savings_percent
            individual[0][i] = health_investment_percent/total_values
            individual[1][i] = life_investment_percent/total_values
            individual[2][i] = savings_percent/total_values
        
        return individual

    def generate_children(self, population):
        children = []
        for _ in range(self.num_children // 2):
            parents = random.sample(population, 2)
            divider = random.randint(0, self.num_periods - 1)
            children.append(self.mutate([parents[0][0][:divider] + parents[1][0][divider:],parents[0][1][:divider] + parents[1][1][divider:],parents[0][2][:divider] + parents[1][2][divider:]]))
            children.append(self.mutate([parents[1][0][:divider] + parents[0][0][divider:],parents[1][1][:divider] + parents[0][1][divider:],parents[1][2][:divider] + parents[0][2][divider:]]))
        return children

    def tournament(self, new_population):
        trimmed_population = []
        for _ in range(self.population_size):
            samples = [new_population[random.randint(0, len(new_population) - 1)] for _ in range(4)]
            lst_fitness = [self.fitness_calculation(samples[i])[0] for i in range(4)]
            trimmed_population.append(samples[lst_fitness.index(max(lst_fitness))])
        return trimmed_population

    def survival(self, population):
        children = self.generate_children(population)
        new_population = population + children
        return self.tournament(new_population)

    def ga_algorithm(self):
        initial_population = self.generate_population()
        current_population = initial_population
        population_profile = []
        for _ in range(4000):
            trimmed_population = self.survival(current_population)
            population_profile.append(trimmed_population)
            current_population = trimmed_population
        return current_population, population_profile

    def lst_enjoyment(self, population_profile):
        enjoyment_profile = []
        for i in range(len(population_profile)):
            enjoyment_profile.append(max([self.fitness_calculation(population_profile[i][j])[0] for j in range(len(population_profile[0]))]))
        return enjoyment_profile
  
meta_parameters = {"population_size" : 100, "num_children": 50, "num_periods": 8, "initial_health": 60, "mutate_prob": 0.05}

ga_healthcare = HealthCare(meta_parameters)

current_population, population_profile = ga_healthcare.ga_algorithm()

enjoyment_profile = ga_healthcare.lst_enjoyment(population_profile)

plt.plot(enjoyment_profile)
plt.ylabel('Total enjoyment')
plt.xlabel('Number of generations')
plt.show()

print(population_profile)