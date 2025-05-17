# This module will handle simulations related to Input Cost Dynamics & Margin Structure. 

class FertilizerPricePassThrough:
    def model_elasticity(self, fertilizer_type: str, crop: str):
        """
        Model fertilizer price pass-through elasticity.
        - Nitrogen price-crop price correlation analysis
        - Phosphate cost impact by crop type differentiation
        - Potash supply concentration risk premium
        - Application rate adjustment behavior by farmer segment
        - Input substitution potential assessment
        """
        pass

class EnergyCostTransmission:
    def simulate_dynamics(self, energy_source: str, crop: str):
        """
        Simulate energy cost transmission dynamics.
        - Direct fuel cost pass-through to production
        - Indirect energy embedded in inputs (especially fertilizer)
        - Drying and processing energy intensity by crop
        - Irrigation energy requirement variation by region
        - Transportation fuel cost margin impact quantification
        """
        pass

class FertilizerCostImpact:
    """
    Analyzes the impact of fertilizer price volatility on farm input costs and profitability.
    Covers Nitrogen (N), Phosphorus (P), and Potassium (K) based fertilizers.
    """

    def __init__(self, baseline_prices=None, crop_nutrient_needs=None):
        """
        Initializes the FertilizerCostImpact analyzer.

        Args:
            baseline_prices (dict, optional): Baseline prices for key fertilizer components.
                                            Example: {'urea_usd_per_tonne': 500, 'dap_usd_per_tonne': 700, 'potash_usd_per_tonne': 600}
            crop_nutrient_needs (dict, optional): Nutrient requirements for different crops.
                                                 Example: {'wheat_kg_per_ha': {'N': 120, 'P': 50, 'K': 70}}
        """
        self.baseline_prices = baseline_prices if baseline_prices else {
            'urea_usd_per_tonne': 350,       # Approx 46% N
            'dap_usd_per_tonne': 500,        # Approx 18% N, 46% P2O5
            'potash_usd_per_tonne': 400,     # Approx 60% K2O
            'ammonium_sulfate_usd_per_tonne': 250 # Approx 21% N
        }
        # Source: FAO, World Bank commodity prices (averages, can be highly volatile)
        self.nutrient_composition = {
            'urea': {'N': 0.46},
            'dap': {'N': 0.18, 'P2O5': 0.46}, # P2O5 to P is approx 0.43
            'potash': {'K2O': 0.60},        # K2O to K is approx 0.83
            'ammonium_sulfate': {'N': 0.21}
        }
        self.crop_nutrient_needs_kg_per_ha = crop_nutrient_needs if crop_nutrient_needs else {
            'wheat_grain': {'N': 100, 'P': 20, 'K': 30}, # P and K are P2O5 and K2O equivalent needs for soil
            'corn_grain': {'N': 150, 'P': 30, 'K': 40},
            'rice_paddy': {'N': 80, 'P': 25, 'K': 25},
            'soybeans': {'N': 20, 'P': 20, 'K': 30} # N fixed from atmosphere, but starter N often applied
        }
        # Price transmission elasticity: How much of a fertilizer price change passes to farmgate crop price
        # This is complex and varies, placeholder value
        self.price_transmission_elasticity = 0.3 

    def calculate_fertilizer_cost_per_ha(self, crop, current_prices=None, application_rates_kg_per_ha=None):
        """
        Calculates the fertilizer cost per hectare for a given crop.
        Uses simplified logic: assumes direct application of N, P, K needs using representative fertilizers.
        A more complex model would optimize fertilizer mix based on price and nutrient content.

        Args:
            crop (str): The crop for which to calculate fertilizer costs (e.g., 'wheat_grain').
            current_prices (dict, optional): Current prices for fertilizers. Defaults to baseline.
            application_rates_kg_per_ha (dict, optional): Specific application rates. Defaults to crop_nutrient_needs.

        Returns:
            dict: Breakdown of fertilizer costs and total cost per hectare.
                  Example: {'N_cost': 50, 'P_cost': 30, 'K_cost': 40, 'total_cost_per_ha': 120}
        """
        if crop not in self.crop_nutrient_needs_kg_per_ha:
            return {"error": f"Crop '{crop}' not found in nutrient needs data."}

        prices = current_prices if current_prices else self.baseline_prices
        needs = application_rates_kg_per_ha if application_rates_kg_per_ha else self.crop_nutrient_needs_kg_per_ha[crop]

        cost_details = {}
        total_cost = 0

        # Nitrogen: Assume Urea is the primary source for N
        if 'N' in needs and 'urea_usd_per_tonne' in prices and self.nutrient_composition['urea']['N'] > 0:
            # Tonnes of Urea needed per ha = (kg N needed / %N in Urea) / 1000
            tonnes_urea_per_ha = (needs['N'] / self.nutrient_composition['urea']['N']) / 1000
            cost_n = tonnes_urea_per_ha * prices['urea_usd_per_tonne']
            cost_details['N_source_fertilizer'] = 'urea'
            cost_details['N_kg_per_ha'] = needs['N']
            cost_details['N_cost_usd_per_ha'] = round(cost_n, 2)
            total_cost += cost_n
        
        # Phosphorus: Assume DAP is the primary source for P2O5
        if 'P' in needs and 'dap_usd_per_tonne' in prices and self.nutrient_composition['dap']['P2O5'] > 0:
            # Tonnes of DAP needed per ha = (kg P2O5 needed / %P2O5 in DAP) / 1000
            tonnes_dap_per_ha = (needs['P'] / self.nutrient_composition['dap']['P2O5']) / 1000
            cost_p = tonnes_dap_per_ha * prices['dap_usd_per_tonne']
            cost_details['P_source_fertilizer'] = 'dap' # DAP also supplies N, this simplified model doesn't net it out.
            cost_details['P2O5_kg_per_ha'] = needs['P']
            cost_details['P_cost_usd_per_ha'] = round(cost_p, 2)
            total_cost += cost_p

        # Potassium: Assume Potash (MOP) is the primary source for K2O
        if 'K' in needs and 'potash_usd_per_tonne' in prices and self.nutrient_composition['potash']['K2O'] > 0:
            # Tonnes of Potash needed per ha = (kg K2O needed / %K2O in Potash) / 1000
            tonnes_potash_per_ha = (needs['K'] / self.nutrient_composition['potash']['K2O']) / 1000
            cost_k = tonnes_potash_per_ha * prices['potash_usd_per_tonne']
            cost_details['K_source_fertilizer'] = 'potash'
            cost_details['K2O_kg_per_ha'] = needs['K']
            cost_details['K_cost_usd_per_ha'] = round(cost_k, 2)
            total_cost += cost_k
            
        cost_details['total_fertilizer_cost_usd_per_ha'] = round(total_cost, 2)
        return cost_details

    def simulate_price_impact_on_farm_costs(self, crop, percentage_change_urea=0, percentage_change_dap=0, percentage_change_potash=0):
        """
        Simulates the impact of percentage changes in fertilizer prices on per-hectare costs for a crop.

        Args:
            crop (str): The crop to analyze.
            percentage_change_urea (float): Percentage change in Urea price (e.g., 10 for 10% increase).
            percentage_change_dap (float): Percentage change in DAP price.
            percentage_change_potash (float): Percentage change in Potash price.

        Returns:
            dict: Analysis including baseline costs, new costs, and the change.
        """
        baseline_cost_details = self.calculate_fertilizer_cost_per_ha(crop, self.baseline_prices)
        if "error" in baseline_cost_details:
            return baseline_cost_details

        new_prices = self.baseline_prices.copy()
        if 'urea_usd_per_tonne' in new_prices:
            new_prices['urea_usd_per_tonne'] *= (1 + percentage_change_urea / 100)
        if 'dap_usd_per_tonne' in new_prices:
            new_prices['dap_usd_per_tonne'] *= (1 + percentage_change_dap / 100)
        if 'potash_usd_per_tonne' in new_prices:
            new_prices['potash_usd_per_tonne'] *= (1 + percentage_change_potash / 100)

        new_cost_details = self.calculate_fertilizer_cost_per_ha(crop, new_prices)
        if "error" in new_cost_details:
            return new_cost_details # Should not happen if baseline was okay

        change_in_cost = new_cost_details['total_fertilizer_cost_usd_per_ha'] - baseline_cost_details['total_fertilizer_cost_usd_per_ha']
        
        return {
            "crop": crop,
            "price_changes_percent": {
                "urea": percentage_change_urea,
                "dap": percentage_change_dap,
                "potash": percentage_change_potash
            },
            "baseline_total_cost_usd_per_ha": baseline_cost_details['total_fertilizer_cost_usd_per_ha'],
            "new_total_cost_usd_per_ha": new_cost_details['total_fertilizer_cost_usd_per_ha'],
            "change_in_cost_usd_per_ha": round(change_in_cost, 2),
            "baseline_cost_breakdown": baseline_cost_details,
            "new_cost_breakdown": new_cost_details
        }

    def assess_impact_on_profitability(self, crop, yield_tonne_per_ha, farmgate_price_usd_per_tonne, fertilizer_cost_usd_per_ha, other_costs_usd_per_ha):
        """
        Assesses the impact of fertilizer costs on overall farm profitability for a given crop.

        Args:
            crop (str): The crop.
            yield_tonne_per_ha (float): Expected yield in tonnes per hectare.
            farmgate_price_usd_per_tonne (float): Expected farmgate price for the crop.
            fertilizer_cost_usd_per_ha (float): Calculated fertilizer cost per hectare.
            other_costs_usd_per_ha (float): Other production costs (seed, labor, fuel, etc.) per hectare.

        Returns:
            dict: Profitability analysis (revenue, total costs, net profit/loss per ha).
        """
        revenue_per_ha = yield_tonne_per_ha * farmgate_price_usd_per_tonne
        total_costs_per_ha = fertilizer_cost_usd_per_ha + other_costs_usd_per_ha
        net_profit_per_ha = revenue_per_ha - total_costs_per_ha

        return {
            "crop": crop,
            "yield_tonne_per_ha": yield_tonne_per_ha,
            "farmgate_price_usd_per_tonne": farmgate_price_usd_per_tonne,
            "revenue_usd_per_ha": round(revenue_per_ha, 2),
            "fertilizer_cost_usd_per_ha": round(fertilizer_cost_usd_per_ha, 2),
            "other_costs_usd_per_ha": round(other_costs_usd_per_ha, 2),
            "total_production_cost_usd_per_ha": round(total_costs_per_ha, 2),
            "net_profit_or_loss_usd_per_ha": round(net_profit_per_ha, 2),
            "fertilizer_cost_as_percent_of_total_cost": round((fertilizer_cost_usd_per_ha / total_costs_per_ha) * 100, 1) if total_costs_per_ha > 0 else 0
        }

class EnergyCostAnalysis:
    """
    Analyzes the impact of energy price changes (fuel, electricity, gas) on farm operational costs.
    Considers direct energy use (machinery, irrigation, drying) and indirect (fertilizers).
    """

    def __init__(self, baseline_energy_prices=None, farm_energy_consumption_profile=None):
        """
        Initializes the EnergyCostAnalysis.

        Args:
            baseline_energy_prices (dict, optional): Baseline prices for key energy sources.
                                                    Example: {'diesel_usd_per_liter': 1.0,
                                                              'electricity_usd_per_kwh': 0.15,
                                                              'natural_gas_usd_per_mcf': 5.0}
            farm_energy_consumption_profile (dict, optional): Typical energy consumption for different farm types/crops.
                                                            Example: {
                                                                'corn_belt_farm_avg_ha': {
                                                                    'diesel_liters_per_ha': 100,
                                                                    'electricity_kwh_per_ha_irrigation': 500, # if irrigated
                                                                    'natural_gas_mcf_per_tonne_drying': 0.5 # for corn drying
                                                                }
                                                            }
        """
        self.baseline_energy_prices = baseline_energy_prices if baseline_energy_prices else {
            'diesel_usd_per_liter': 0.80, # Global average can vary widely
            'electricity_usd_per_kwh': 0.12,
            'natural_gas_usd_per_mbtu': 4.0, # Million British Thermal Units
            'lpg_usd_per_gallon': 2.5
        }
        # Profile per hectare or per unit of production for representative farm types
        self.farm_energy_consumption_profile = farm_energy_consumption_profile if farm_energy_consumption_profile else {
            'large_scale_grain_farm_midwest_usa_ha': {
                'diesel_operations_liter': 120, # Tillage, planting, spraying, harvest
                'electricity_irrigation_kwh': 300, # For a portion of land that is irrigated
                'natural_gas_drying_mbtu_per_tonne_corn': 0.6,
                'indirect_fertilizer_energy_equivalent_mbtu': 5 # Energy embedded in typical fertilizer application
            },
            'brazilian_sugarcane_farm_ha': {
                'diesel_operations_liter': 150,
                'bagasse_cogeneration_kwh_surplus_per_tonne_cane': -20 # Negative indicates energy production
            },
            'indian_wheat_farm_smallholder_ha':{
                'diesel_operations_liter': 60,
                'electricity_irrigation_kwh': 800 # Often heavily subsidized
            }
        }
        self.energy_sources = ['diesel', 'electricity', 'natural_gas', 'lpg', 'indirect_fertilizer_energy']

    def calculate_direct_energy_cost(self, farm_type, area_ha, current_energy_prices):
        """
        Calculates the direct energy cost for a given farm type and area based on current prices.

        Args:
            farm_type (str): Key from self.farm_energy_consumption_profile.
            area_ha (float): Total area in hectares.
            current_energy_prices (dict): Current prices for energy sources.
                                          Example: {'diesel_usd_per_liter': 1.2, 'electricity_usd_per_kwh': 0.18}

        Returns:
            dict: Detailed direct energy costs and total.
                  Example: {'diesel_cost': 12000, 'electricity_cost': 2700, 'total_direct_cost': 14700}
        """
        if farm_type not in self.farm_energy_consumption_profile:
            return {"error": f"Farm type '{farm_type}' not found in profile."}

        profile = self.farm_energy_consumption_profile[farm_type]
        costs = {'total_direct_cost_usd': 0} # Ensure key exists

        # Diesel for operations
        if 'diesel_operations_liter' in profile and 'diesel_usd_per_liter' in current_energy_prices:
            diesel_cost = profile['diesel_operations_liter'] * area_ha * current_energy_prices['diesel_usd_per_liter']
            costs['diesel_operations_cost_usd'] = round(diesel_cost, 2)
            costs['total_direct_cost_usd'] += diesel_cost

        # Electricity for irrigation (or other uses)
        if 'electricity_irrigation_kwh' in profile and 'electricity_usd_per_kwh' in current_energy_prices:
            electricity_cost = profile['electricity_irrigation_kwh'] * area_ha * current_energy_prices['electricity_usd_per_kwh']
            costs['electricity_irrigation_cost_usd'] = round(electricity_cost, 2)
            costs['total_direct_cost_usd'] += electricity_cost
        
        # Natural gas for drying (example for corn)
        # This calculation would need production estimates (tonnes) rather than just area for accuracy
        if 'natural_gas_drying_mbtu_per_tonne_corn' in profile and 'natural_gas_usd_per_mbtu' in current_energy_prices:
            # Placeholder: Assume a yield for calculation, e.g., 10 tonnes/ha for corn
            assumed_yield_tonnes_per_ha = 10 # This should ideally be an input or from a crop model
            total_production_tonnes = assumed_yield_tonnes_per_ha * area_ha
            drying_cost = profile['natural_gas_drying_mbtu_per_tonne_corn'] * total_production_tonnes * current_energy_prices['natural_gas_usd_per_mbtu']
            costs['natural_gas_drying_cost_usd'] = round(drying_cost, 2)
            costs['total_direct_cost_usd'] += drying_cost

        costs['total_direct_cost_usd'] = round(costs['total_direct_cost_usd'], 2)
        return costs

    def analyze_price_change_impact(self, farm_type, area_ha, percentage_change_diesel=0, percentage_change_electricity=0, percentage_change_natural_gas=0):
        """
        Analyzes the impact of percentage changes in key energy prices on direct costs.

        Args:
            farm_type (str): Key from self.farm_energy_consumption_profile.
            area_ha (float): Total area in hectares.
            percentage_change_diesel (float): Percentage change in diesel price (e.g., 10 for 10% increase).
            percentage_change_electricity (float): Percentage change in electricity price.
            percentage_change_natural_gas (float): Percentage change in natural gas price.

        Returns:
            dict: Cost impact analysis.
                  Example: {'baseline_costs': {...}, 'new_costs': {...}, 'cost_increase_usd': ..., 'cost_increase_percent': ...}
        """
        baseline_direct_costs = self.calculate_direct_energy_cost(farm_type, area_ha, self.baseline_energy_prices)
        if "error" in baseline_direct_costs:
            return baseline_direct_costs

        new_prices = self.baseline_energy_prices.copy()
        if 'diesel_usd_per_liter' in new_prices: # Ensure key exists before modifying
            new_prices['diesel_usd_per_liter'] *= (1 + percentage_change_diesel / 100)
        if 'electricity_usd_per_kwh' in new_prices:
            new_prices['electricity_usd_per_kwh'] *= (1 + percentage_change_electricity / 100)
        if 'natural_gas_usd_per_mbtu' in new_prices:
            new_prices['natural_gas_usd_per_mbtu'] *= (1 + percentage_change_natural_gas / 100)

        new_direct_costs = self.calculate_direct_energy_cost(farm_type, area_ha, new_prices)
        if "error" in new_direct_costs:
             return new_direct_costs

        cost_increase_usd = new_direct_costs['total_direct_cost_usd'] - baseline_direct_costs['total_direct_cost_usd']
        cost_increase_percent = 0
        if baseline_direct_costs['total_direct_cost_usd'] > 0:
            cost_increase_percent = (cost_increase_usd / baseline_direct_costs['total_direct_cost_usd']) * 100
        
        return {
            'farm_type': farm_type,
            'area_ha': area_ha,
            'price_changes_percent': {
                'diesel': percentage_change_diesel,
                'electricity': percentage_change_electricity,
                'natural_gas': percentage_change_natural_gas
            },
            'baseline_total_direct_cost_usd': baseline_direct_costs['total_direct_cost_usd'],
            'new_total_direct_cost_usd': new_direct_costs['total_direct_cost_usd'],
            'change_in_total_direct_cost_usd': round(cost_increase_usd, 2), # Added this key
            'cost_increase_percent': round(cost_increase_percent, 2)
        }

    def estimate_indirect_energy_cost_impact(self, farm_type, area_ha, energy_price_change_percent):
        """
        Estimates the impact of general energy price changes on indirect costs (e.g., fertilizers).
        This is a simplified estimation, assuming natural gas is a proxy for energy in fertilizer production.

        Args:
            farm_type (str): Key from self.farm_energy_consumption_profile.
            area_ha (float): Total area in hectares.
            energy_price_change_percent (float): General percentage change in energy prices (applied to natural gas as proxy).

        Returns:
            dict: Estimated indirect cost impact.
        """
        if farm_type not in self.farm_energy_consumption_profile:
            return {"error": f"Farm type '{farm_type}' not found in profile."}
        
        profile = self.farm_energy_consumption_profile[farm_type]
        if 'indirect_fertilizer_energy_equivalent_mbtu' not in profile or 'natural_gas_usd_per_mbtu' not in self.baseline_energy_prices:
            return {"info": "Indirect energy cost data or baseline natural gas price not available for this farm type."}

        baseline_ng_price = self.baseline_energy_prices['natural_gas_usd_per_mbtu']
        baseline_indirect_energy_cost_per_ha = profile['indirect_fertilizer_energy_equivalent_mbtu'] * baseline_ng_price
        
        new_natural_gas_price = baseline_ng_price * (1 + energy_price_change_percent / 100)
        new_indirect_energy_cost_per_ha = profile['indirect_fertilizer_energy_equivalent_mbtu'] * new_natural_gas_price
        
        total_baseline_indirect_cost = baseline_indirect_energy_cost_per_ha * area_ha
        total_new_indirect_cost = new_indirect_energy_cost_per_ha * area_ha
        change_in_indirect_cost = total_new_indirect_cost - total_baseline_indirect_cost

        return {
            'farm_type': farm_type,
            'area_ha': area_ha,
            'general_energy_price_change_percent_applied_to_ng': energy_price_change_percent,
            'estimated_baseline_indirect_fertilizer_energy_cost_usd': round(total_baseline_indirect_cost, 2),
            'estimated_new_indirect_fertilizer_energy_cost_usd': round(total_new_indirect_cost, 2),
            'estimated_change_in_indirect_cost_usd': round(change_in_indirect_cost, 2)
        }

class SeedCostTechnologyImpact: # Placeholder
    def simulate_impact(self, seed_type: str, crop: str):
        pass

class LaborCostAvailability: # Placeholder
    def track_stress_points(self, region: str, worker_type: str):
        pass

class FarmMachineryOperationalCost: # Placeholder
    def calculate_cost(self, machinery_type: str, operation_hours: float, fuel_price_usd_per_liter: float):
        pass

class PostHarvestCostDynamics: # Placeholder
    def simulate_dynamics(self, crop: str):
        pass

class MarginPressureIndex: # Placeholder
    def calculate_index(self, crop: str, margin: float):
        pass

class LabourCostDynamics:
    """
    Models dynamics in agricultural labor costs, including wage rates, availability,
    impact of mechanization, and programs like H-2A.
    """

    def __init__(self, baseline_wage_rates=None, regional_data=None, mechanization_options=None):
        self.baseline_wage_rates = baseline_wage_rates if baseline_wage_rates else {
            'us_avg_field_worker': 17.55, 
            'us_avg_equip_operator': 18.47, 
            'us_avg_supervisor': 25.61, 
            'ca_aewr_general_2023': 19.75, 
            'fl_aewr_custom_harvesters_2024': 14.69,
            'developing_country_general': 2.50 
        }
        self.regional_labor_profile = regional_data if regional_data else {
            'grain_avg': { 'pre_harvest_hrs': 1.5, 'harvest_hrs': 1.0, 'total_hrs': 2.5 },
            'fruit_manual_hg': { 'pre_harvest_hrs': 200, 'harvest_hrs': 1000, 'total_hrs': 1200 },
            'veg_mixed_hg': { 'pre_harvest_hrs': 100, 'harvest_hrs': 300, 'total_hrs': 400 }
        }
        self.mechanization_options = mechanization_options if mechanization_options else {
            'fruit_harvest_assist': {
                'cost_usd': 25000, 'efficiency_gain_percent': 15,
                'maint_usd_annual': 1000, 'lifespan_yr': 8, 'ops_cost_hr_usd': 5
            },
            'robotic_harvester_prototype': { 
                'cost_usd': 300000, 'labor_reduction_percent': 70,
                'maint_usd_annual': 20000, 'lifespan_yr': 5,
                'skilled_op_hr_day': 8, 'skilled_op_wage_hr_usd': 30, 'ops_cost_hr_usd': 20
            }
        }
        self.h2a_additional_costs_per_worker_usd = {
            'transport_intl_roundtrip': 600, 
            'housing_monthly': 400, 
            'admin_fees_total': 500
        }
        self.avg_h2a_season_months = 5.75

    def calculate_labor_cost_per_ha(self, crop_profile_key, wage_key, hours_override=None):
        if crop_profile_key not in self.regional_labor_profile or wage_key not in self.baseline_wage_rates:
            return {"error": "Invalid crop profile or wage key."}
        
        hours = hours_override if hours_override is not None else self.regional_labor_profile[crop_profile_key]['total_hrs']
        rate = self.baseline_wage_rates[wage_key]
        cost = hours * rate
        return {
            'crop_profile': crop_profile_key, 'wage_key': wage_key, 
            'labor_hrs_per_ha': hours, 'wage_rate_usd_per_hr': rate, 
            'total_labor_cost_usd_per_ha': round(cost, 2)
        }

    def analyze_wage_rate_impact(self, crop_profile_key, wage_key, new_rate=None, percent_increase=None):
        base_calc = self.calculate_labor_cost_per_ha(crop_profile_key, wage_key)
        if "error" in base_calc: return base_calc

        actual_new_rate = 0
        if new_rate is not None: actual_new_rate = new_rate
        elif percent_increase is not None: actual_new_rate = base_calc['wage_rate_usd_per_hr'] * (1 + percent_increase / 100)
        else: return {"error": "New rate or percentage increase needed."}

        new_cost = base_calc['labor_hrs_per_ha'] * actual_new_rate
        return {
            'crop_profile': crop_profile_key, 
            'base_wage_usd_hr': base_calc['wage_rate_usd_per_hr'], 
            'base_cost_usd_ha': base_calc['total_labor_cost_usd_per_ha'],
            'new_wage_usd_hr': round(actual_new_rate, 2), 
            'new_cost_usd_ha': round(new_cost, 2),
            'cost_increase_usd_ha': round(new_cost - base_calc['total_labor_cost_usd_per_ha'], 2)
        }

    def assess_mechanization_roi(self, mech_key, crop_key, wage_key, area_ha, annual_op_hrs=None):
        if mech_key not in self.mechanization_options: return {"error": "Mechanization key not found."}
        machine = self.mechanization_options[mech_key]
        base_labor = self.calculate_labor_cost_per_ha(crop_key, wage_key)
        if "error" in base_labor: return base_labor

        base_total_cost = base_labor['total_labor_cost_usd_per_ha'] * area_ha
        base_total_hrs = base_labor['labor_hrs_per_ha'] * area_ha

        reduction_pct = machine.get('labor_reduction_percent', machine.get('efficiency_gain_percent', 0))
        hrs_saved = base_total_hrs * (reduction_pct / 100)
        labor_cost_saved = hrs_saved * base_labor['wage_rate_usd_per_hr']
        remaining_hrs = base_total_hrs - hrs_saved
        remaining_labor_cost = remaining_hrs * base_labor['wage_rate_usd_per_hr']

        machine_ops_cost = 0
        if annual_op_hrs and 'ops_cost_hr_usd' in machine:
            machine_ops_cost = annual_op_hrs * machine['ops_cost_hr_usd']
        
        skilled_op_cost = 0
        if 'skilled_op_hr_day' in machine and annual_op_hrs:
            skilled_op_total_hrs = annual_op_hrs 
            skilled_op_cost = skilled_op_total_hrs * machine.get('skilled_op_wage_hr_usd', base_labor['wage_rate_usd_per_hr'] * 1.5)

        total_cost_with_machine = remaining_labor_cost + machine['maint_usd_annual'] + machine_ops_cost + skilled_op_cost
        net_annual_savings = base_total_cost - total_cost_with_machine
        
        roi_pct = (net_annual_savings / machine['cost_usd']) * 100 if machine['cost_usd'] > 0 else float('inf')
        payback_yr = machine['cost_usd'] / net_annual_savings if net_annual_savings > 0 else float('inf')

        return {
            'mech_option': mech_key, 'area_ha': area_ha,
            'base_annual_labor_cost_usd': round(base_total_cost, 2),
            'est_annual_cost_w_machine_usd': round(total_cost_with_machine, 2),
            'net_annual_savings_usd': round(net_annual_savings, 2),
            'investment_usd': machine['cost_usd'],
            'simple_roi_pct_annual': round(roi_pct, 2),
            'payback_years': round(payback_yr, 1) if payback_yr != float('inf') else 'N/A'
        }

    def estimate_h2a_labor_cost(self, num_workers, wage_key_aewr, season_months_override=None):
        if wage_key_aewr not in self.baseline_wage_rates: return {"error": "AEWR key not found."}
        
        aewr = self.baseline_wage_rates[wage_key_aewr]
        months = season_months_override if season_months_override is not None else self.avg_h2a_season_months
        
        hrs_per_worker_season = 40 * 4.33 * months
        wage_cost_per_worker = hrs_per_worker_season * aewr
        
        additional_cost_per_worker = (
            self.h2a_additional_costs_per_worker_usd['transport_intl_roundtrip'] +
            self.h2a_additional_costs_per_worker_usd['housing_monthly'] * months +
            self.h2a_additional_costs_per_worker_usd['admin_fees_total']
        )
        total_cost_per_worker = wage_cost_per_worker + additional_cost_per_worker
        overall_total = total_cost_per_worker * num_workers

        return {
            'num_workers': num_workers, 'season_months': months, 'aewr_usd_hr': aewr,
            'est_wage_cost_per_worker_usd': round(wage_cost_per_worker, 2),
            'est_addl_costs_per_worker_usd': round(additional_cost_per_worker, 2),
            'est_total_cost_per_worker_usd': round(total_cost_per_worker, 2),
            'overall_est_h2a_cost_usd': round(overall_total, 2)
        }

class AgriInputPriceIndex:
    """
    Models an agricultural input price index.
    """
    def __init__(self, baseline_year=2023):
        self.baseline_year = baseline_year
        self.weights = {
            "fertilizer": 0.25, "seed": 0.10, "pesticides": 0.10, "fuel": 0.15,
            "machinery_purchase_repair": 0.15, "labour": 0.15, "utilities_other": 0.10
        }
        self.component_prices = {cat: 100.0 for cat in self.weights.keys()}
        self.current_index_value = self._calculate_index()

    def _calculate_index(self):
        val = sum(self.component_prices.get(comp, 100.0) * wt for comp, wt in self.weights.items())
        return round(val, 2)

    def update_component_price(self, component_name, new_price_index):
        if component_name in self.component_prices:
            self.component_prices[component_name] = new_price_index
            self.current_index_value = self._calculate_index()
            # print(f"Updated {component_name} to {new_price_index}. New index: {self.current_index_value}")
            return self.current_index_value
        # print(f"Warning: Component '{component_name}' not found.")
        return self.current_index_value

    def get_index_value(self): return self.current_index_value
    def get_component_prices(self): return self.component_prices
    def reset_to_baseline(self):
        self.component_prices = {cat: 100.0 for cat in self.weights.keys()}
        self.current_index_value = self._calculate_index()
        # print(f"Index reset. Value: {self.current_index_value}")

class FarmMarginModel:
    """
    Calculates farm margins (gross and net) and break-even points for a specific crop enterprise.
    """
    def __init__(self, crop_name: str, expected_yield_t_per_ha: float, market_price_usd_per_t: float, 
                 variable_costs_usd_per_ha: dict, fixed_costs_usd_per_ha: float = 0):
        self.crop_name = crop_name
        self.expected_yield_t_per_ha = expected_yield_t_per_ha
        self.market_price_usd_per_t = market_price_usd_per_t
        self.variable_costs_usd_per_ha = variable_costs_usd_per_ha.copy() # Ensure a copy
        self.fixed_costs_usd_per_ha = fixed_costs_usd_per_ha

        self.total_variable_costs_usd_per_ha = sum(self.variable_costs_usd_per_ha.values())
        self.total_costs_usd_per_ha = self.total_variable_costs_usd_per_ha + self.fixed_costs_usd_per_ha

    def calculate_gross_revenue_per_ha(self, yield_t_per_ha=None, price_usd_per_t=None):
        y = yield_t_per_ha if yield_t_per_ha is not None else self.expected_yield_t_per_ha
        p = price_usd_per_t if price_usd_per_t is not None else self.market_price_usd_per_t
        return y * p

    def get_total_variable_costs_per_ha(self): return self.total_variable_costs_usd_per_ha
    def get_total_fixed_costs_per_ha(self): return self.fixed_costs_usd_per_ha
    def get_total_costs_per_ha(self): return self.total_costs_usd_per_ha

    def calculate_gross_margin_per_ha(self, gross_revenue_usd_per_ha=None):
        rev = gross_revenue_usd_per_ha if gross_revenue_usd_per_ha is not None else self.calculate_gross_revenue_per_ha()
        return rev - self.total_variable_costs_usd_per_ha

    def calculate_net_margin_per_ha(self, gross_revenue_usd_per_ha=None):
        rev = gross_revenue_usd_per_ha if gross_revenue_usd_per_ha is not None else self.calculate_gross_revenue_per_ha()
        return rev - self.total_costs_usd_per_ha
    
    def calculate_net_margin_percent(self, gross_revenue_usd_per_ha=None):
        rev = gross_revenue_usd_per_ha if gross_revenue_usd_per_ha is not None else self.calculate_gross_revenue_per_ha()
        net_margin = self.calculate_net_margin_per_ha(gross_revenue_usd_per_ha=rev)
        return (net_margin / rev) * 100 if rev != 0 else 0.0

    def calculate_break_even_yield_t_per_ha(self, price_usd_per_t=None):
        p = price_usd_per_t if price_usd_per_t is not None else self.market_price_usd_per_t
        return self.total_costs_usd_per_ha / p if p != 0 else float('inf')

    def calculate_break_even_price_usd_per_t(self, yield_t_per_ha=None):
        y = yield_t_per_ha if yield_t_per_ha is not None else self.expected_yield_t_per_ha
        return self.total_costs_usd_per_ha / y if y != 0 else float('inf')

    def get_full_margin_analysis(self, yield_t_per_ha=None, price_usd_per_t=None):
        cy = yield_t_per_ha if yield_t_per_ha is not None else self.expected_yield_t_per_ha
        cp = price_usd_per_t if price_usd_per_t is not None else self.market_price_usd_per_t
        gr = self.calculate_gross_revenue_per_ha(cy, cp)
        gm = self.calculate_gross_margin_per_ha(gr)
        nm = self.calculate_net_margin_per_ha(gr)
        nmp = self.calculate_net_margin_percent(gr)
        bey = self.calculate_break_even_yield_t_per_ha(cp)
        bep = self.calculate_break_even_price_usd_per_t(cy)
        return {
            "crop_name": self.crop_name, "yield_t_per_ha": cy, "price_usd_per_t": cp,
            "gross_revenue_usd_per_ha": round(gr, 2),
            "variable_costs_detail_usd_per_ha": {k: round(v,2) for k,v in self.variable_costs_usd_per_ha.items()},
            "total_variable_costs_usd_per_ha": round(self.total_variable_costs_usd_per_ha, 2),
            "total_fixed_costs_usd_per_ha": round(self.fixed_costs_usd_per_ha, 2),
            "total_costs_usd_per_ha": round(self.total_costs_usd_per_ha, 2),
            "gross_margin_usd_per_ha": round(gm, 2), "net_margin_usd_per_ha": round(nm, 2),
            "net_margin_percent": round(nmp, 2),
            "break_even_yield_t_per_ha": round(bey, 2) if bey != float('inf') else 'N/A',
            "break_even_price_usd_per_t": round(bep, 2) if bep != float('inf') else 'N/A'
        }

class InputCostSensitivityAnalysis:
    """
    Performs sensitivity analysis on farm margins by varying input costs or output price.
    """
    def __init__(self, farm_margin_model: FarmMarginModel):
        self.farm_margin_model = farm_margin_model
        self.base_analysis = self.farm_margin_model.get_full_margin_analysis()
        self.base_net_margin = self.base_analysis['net_margin_usd_per_ha']

    def analyze_input_cost_sensitivity(self, cost_component_key: str, percentage_change: float):
        if cost_component_key not in self.farm_margin_model.variable_costs_usd_per_ha:
            return {"error": f"Cost component '{cost_component_key}' not found in var costs.", "available_keys": list(self.farm_margin_model.variable_costs_usd_per_ha.keys())}

        original_cost = self.farm_margin_model.variable_costs_usd_per_ha[cost_component_key]
        new_var_costs = self.farm_margin_model.variable_costs_usd_per_ha.copy()
        new_var_costs[cost_component_key] = original_cost * (1 + percentage_change / 100)

        temp_model = FarmMarginModel(
            crop_name=self.farm_margin_model.crop_name,
            expected_yield_t_per_ha=self.farm_margin_model.expected_yield_t_per_ha,
            market_price_usd_per_t=self.farm_margin_model.market_price_usd_per_t,
            variable_costs_usd_per_ha=new_var_costs,
            fixed_costs_usd_per_ha=self.farm_margin_model.fixed_costs_usd_per_ha
        )
        new_analysis = temp_model.get_full_margin_analysis()
        new_net_margin = new_analysis['net_margin_usd_per_ha']
        return {
            "cost_key": cost_component_key, "percent_change_cost": percentage_change,
            "base_net_margin_usd_ha": self.base_net_margin,
            "new_net_margin_usd_ha": new_net_margin,
            "change_net_margin_usd_ha": round(new_net_margin - self.base_net_margin, 2),
            "new_cost_value_usd_ha": round(new_var_costs[cost_component_key], 2)
        }

    def analyze_price_sensitivity(self, percentage_change_in_price: float):
        new_price = self.farm_margin_model.market_price_usd_per_t * (1 + percentage_change_in_price / 100)
        # Use the original model, but provide the new price to its analysis method
        new_analysis = self.farm_margin_model.get_full_margin_analysis(price_usd_per_t=new_price)
        new_net_margin = new_analysis['net_margin_usd_per_ha']
        return {
            "percent_change_price": percentage_change_in_price,
            "base_price_usd_t": self.farm_margin_model.market_price_usd_per_t,
            "new_price_usd_t": round(new_price, 2),
            "base_net_margin_usd_ha": self.base_net_margin,
            "new_net_margin_usd_ha": new_net_margin,
            "change_net_margin_usd_ha": round(new_net_margin - self.base_net_margin, 2)
        }

    def run_scenario_analysis(self, cost_changes: dict = None, price_change_percent: float = None):
        new_var_costs = self.farm_margin_model.variable_costs_usd_per_ha.copy()
        if cost_changes:
            for key, change in cost_changes.items():
                if key in new_var_costs: 
                    new_var_costs[key] *= (1 + change / 100)
                else:
                    print(f"Warning: Cost key '{key}' for scenario not in variable costs. Skipping.")
        
        new_price = self.farm_margin_model.market_price_usd_per_t
        if price_change_percent is not None:
            new_price *= (1 + price_change_percent / 100)

        temp_model = FarmMarginModel(
            self.farm_margin_model.crop_name, 
            self.farm_margin_model.expected_yield_t_per_ha,
            new_price, 
            new_var_costs, 
            self.farm_margin_model.fixed_costs_usd_per_ha
        )
        new_analysis = temp_model.get_full_margin_analysis()
        new_net_margin = new_analysis['net_margin_usd_per_ha']
        return {
            "inputs": {"cost_changes_pct": cost_changes, "price_change_pct": price_change_percent},
            "base_net_margin_usd_ha": self.base_net_margin,
            "new_net_margin_usd_ha": new_net_margin,
            "change_net_margin_usd_ha": round(new_net_margin - self.base_net_margin, 2),
            "full_new_analysis": new_analysis
        }

class InputCostDynamicsMarginStructure:
    """
    Orchestrates analysis of input costs, farm margins, and their sensitivities.
    """
    def __init__(self, baseline_year=2023, region="global_average"):
        self.baseline_year = baseline_year
        self.region = region
        self.fertilizer_model = FertilizerCostImpact()
        self.energy_model = EnergyCostAnalysis()
        self.labour_model = LabourCostDynamics()
        self.agri_input_index = AgriInputPriceIndex(baseline_year=baseline_year)
        self.current_farm_margin_model = None
        self.sensitivity_analyzer = None

    def setup_farm_scenario(self, crop_name, expected_yield, market_price, variable_costs, fixed_costs):
        self.current_farm_margin_model = FarmMarginModel(
            crop_name, expected_yield, market_price, variable_costs, fixed_costs
        )
        self.sensitivity_analyzer = InputCostSensitivityAnalysis(self.current_farm_margin_model)
        print(f"Farm scenario for '{crop_name}' set up. Base net margin: ${self.sensitivity_analyzer.base_net_margin:.2f}/ha")
        return self.current_farm_margin_model

    def simulate_input_price_scenario(self, crop_name="wheat_grain", fertilizer_changes=None, energy_changes=None, labour_changes=None, commodity_price_change_percent=None):
        print(f"\nSimulating scenario for '{crop_name}'...")
        
        # Determine baseline costs for the specific crop for the farm model
        fert_costs_details = self.fertilizer_model.calculate_fertilizer_cost_per_ha(crop_name)
        if "error" in fert_costs_details:
            print(f"Error in fertilizer calc for {crop_name}: {fert_costs_details['error']}")
            return fert_costs_details
        baseline_fert_total_ha = fert_costs_details.get('total_fertilizer_cost_usd_per_ha', 0)

        # Simplified energy and labor for this example farm budget
        # More complex farm types would need different profiles from Energy/Labour models
        baseline_energy_total_ha = 50 
        if crop_name == "corn_grain":
             energy_direct = self.energy_model.calculate_direct_energy_cost('large_scale_grain_farm_midwest_usa_ha', 1, self.energy_model.baseline_energy_prices)
             baseline_energy_total_ha = energy_direct.get('total_direct_cost_usd', 50) # Cost for 1 ha
        elif crop_name == "wheat_grain":
            # Example: slightly different energy for wheat if needed, otherwise default
            baseline_energy_total_ha = 45 

        baseline_labor_total_ha = 100 # Default placeholder
        if crop_name == "wheat_grain" or crop_name == "corn_grain":
             labor_calc = self.labour_model.calculate_labor_cost_per_ha('grain_avg', 'us_avg_field_worker')
             baseline_labor_total_ha = labor_calc.get('total_labor_cost_usd_per_ha', 100)
        
        default_variable_costs_ha = {
            "seed": 60,
            "fertilizer_total": baseline_fert_total_ha,
            "pesticides_herbicides": 45,
            "fuel_machinery_ops": baseline_energy_total_ha, 
            "labor": baseline_labor_total_ha,
            "crop_insurance": 20,
            "other_variable": 30
        }
        default_fixed_costs_ha = 150
        default_yield_t_ha, default_price_usd_t = (4.0, 250) # Wheat defaults
        if crop_name == "corn_grain":
            default_yield_t_ha, default_price_usd_t = (10.0, 180)
        elif crop_name == "rice_paddy":
            default_yield_t_ha, default_price_usd_t = (6.0, 300)
        elif crop_name == "soybeans":
            default_yield_t_ha, default_price_usd_t = (3.0, 450)

        self.setup_farm_scenario(
            crop_name,
            default_yield_t_ha,
            default_price_usd_t,
            default_variable_costs_ha,
            default_fixed_costs_ha
        )
        
        print("Base Farm Analysis for Scenario:")
        for k, v_val in self.current_farm_margin_model.get_full_margin_analysis().items():
            if isinstance(v_val, dict):
                print(f"  {k}:")
                for sk, sv in v_val.items(): print(f"    {sk}: {sv}")
            else:
                print(f"  {k}: {v_val}")

        if not self.sensitivity_analyzer: return {"error": "Farm scenario not set up for sensitivity."}

        scenario_cost_changes_pct = {}
        if fertilizer_changes and 'total_impact_percent' in fertilizer_changes:
            scenario_cost_changes_pct['fertilizer_total'] = fertilizer_changes['total_impact_percent']
        if energy_changes and 'diesel' in energy_changes: 
             scenario_cost_changes_pct['fuel_machinery_ops'] = energy_changes['diesel'] # Assumes diesel % change applies to this category
        if labour_changes and 'field_worker_percent_change' in labour_changes:
            scenario_cost_changes_pct['labor'] = labour_changes['field_worker_percent_change']
        
        print(f"\nRunning Scenario with Cost Changes (%): {scenario_cost_changes_pct}, Price Change (%): {commodity_price_change_percent}")
        results = self.sensitivity_analyzer.run_scenario_analysis(scenario_cost_changes_pct, commodity_price_change_percent)
        
        print("\nSensitivity Scenario Analysis Results:")
        print(f"  Base Net Margin: ${results['base_net_margin_usd_ha']:.2f}/ha")
        print(f"  New Net Margin: ${results['new_net_margin_usd_ha']:.2f}/ha")
        print(f"  Change in Net Margin: ${results['change_net_margin_usd_ha']:.2f}/ha")
        print(f"  Full analysis under scenario: {results['full_new_analysis']}")
        return results

    def get_current_input_price_index(self):
        return {"index_value": self.agri_input_index.get_index_value(), "components": self.agri_input_index.get_component_prices()}

if __name__ == '__main__':
    print("--------- Input Cost Dynamics & Margin Structure Simulation ---------")
    dynamics_orchestrator = InputCostDynamicsMarginStructure(baseline_year=2024)

    print("\n--- Section 1: Fertilizer Cost Analysis ---")
    fertilizer_module = dynamics_orchestrator.fertilizer_model
    wheat_fert_costs = fertilizer_module.calculate_fertilizer_cost_per_ha('wheat_grain')
    print(f"Baseline fertilizer cost for WHEAT: ${wheat_fert_costs.get('total_fertilizer_cost_usd_per_ha', 0):.2f}/ha")
    urea_price_shock_effect = fertilizer_module.simulate_price_impact_on_farm_costs('wheat_grain', percentage_change_urea=20)
    print(f"WHEAT fertilizer cost after +20% Urea price: ${urea_price_shock_effect.get('new_total_cost_usd_per_ha', 0):.2f}/ha (Change: ${urea_price_shock_effect.get('change_in_cost_usd_per_ha',0):.2f}/ha)")
    corn_fert_costs = fertilizer_module.calculate_fertilizer_cost_per_ha('corn_grain')
    print(f"Baseline fertilizer cost for CORN: ${corn_fert_costs.get('total_fertilizer_cost_usd_per_ha', 0):.2f}/ha")

    print("\n--- Section 2: Energy Cost Analysis ---")
    energy_module = dynamics_orchestrator.energy_model
    midwest_farm_energy_cost = energy_module.calculate_direct_energy_cost('large_scale_grain_farm_midwest_usa_ha', 100, energy_module.baseline_energy_prices)
    print(f"Baseline direct energy cost for 100ha Midwest Grain Farm: ${midwest_farm_energy_cost.get('total_direct_cost_usd',0):.2f}")
    energy_price_shock_effect = energy_module.analyze_price_change_impact('large_scale_grain_farm_midwest_usa_ha', 100, percentage_change_diesel=25, percentage_change_electricity=10)
    print(f"Midwest Farm energy cost after diesel +25%, electricity +10%: ${energy_price_shock_effect.get('new_total_direct_cost_usd',0):.2f} (Change: ${energy_price_shock_effect.get('change_in_total_direct_cost_usd',0):.2f})")

    print("\n--- Section 3: Labour Cost Analysis ---")
    labour_module = dynamics_orchestrator.labour_model
    us_grain_labour_cost = labour_module.calculate_labor_cost_per_ha('grain_avg', 'us_avg_field_worker')
    print(f"Baseline labor cost for US average grain farming: ${us_grain_labour_cost.get('total_labor_cost_usd_per_ha',0):.2f}/ha")
    wage_hike_effect = labour_module.analyze_wage_rate_impact('grain_avg', 'us_avg_field_worker', percent_increase=15)
    print(f"US grain farm labor cost after +15% field worker wage: ${wage_hike_effect.get('new_cost_usd_ha',0):.2f}/ha")
    h2a_estimate = labour_module.estimate_h2a_labor_cost(num_workers=10, wage_key_aewr='ca_aewr_general_2023', season_months_override=6)
    print(f"Estimated H2A cost for 10 workers in CA (6 months): ${h2a_estimate.get('overall_est_h2a_cost_usd', 0):.2f}")

    print("\n--- Section 4: Agri-Input Price Index ---")
    input_index_model = dynamics_orchestrator.agri_input_index
    print(f"Initial Input Price Index ({input_index_model.baseline_year}): {input_index_model.get_index_value()}")
    input_index_model.update_component_price("fertilizer", 115) 
    input_index_model.update_component_price("fuel", 125)
    print(f"Updated Input Price Index: {input_index_model.get_index_value()}")
    print(f"Current component prices (indexed): {input_index_model.get_component_prices()}")

    print("\n--- Section 5: Farm Margin Model & Sensitivity Analysis (WHEAT Example) ---")
    wheat_variable_costs_ha = {
        "seed": 70, 
        "fertilizer_total": wheat_fert_costs.get('total_fertilizer_cost_usd_per_ha', 150), 
        "pesticides_herbicides": 50,
        "fuel_machinery_ops": 120, # Placeholder, should be derived from energy model for wheat
        "labor": us_grain_labour_cost.get('total_labor_cost_usd_per_ha', 100),
        "crop_insurance": 25,
        "other_variable": 35
    }
    wheat_fixed_costs_ha = 200
    
    # Setup WHEAT farm scenario using the orchestrator
    dynamics_orchestrator.setup_farm_scenario(
        crop_name="Wheat (Generic)",
        expected_yield=5.0,
        market_price=220,
        variable_costs=wheat_variable_costs_ha,
        fixed_costs=wheat_fixed_costs_ha
    )

    if dynamics_orchestrator.current_farm_margin_model and dynamics_orchestrator.sensitivity_analyzer:
        # Get base margin analysis for WHEAT
        # base_wheat_margin_details = dynamics_orchestrator.current_farm_margin_model.get_full_margin_analysis()
        # print("\nBaseline WHEAT Farm Margin Analysis (Full Details):")
        # for key, val in base_wheat_margin_details.items():
        #     if isinstance(val, dict): 
        #         print(f"  {key}:"); [print(f"    {sk}: {sv}") for sk,sv in val.items()]
        #     else: print(f"  {key}: {val}")

        # Perform sensitivity analysis using the WHEAT farm model initialized above
        wheat_sensitivity_module = dynamics_orchestrator.sensitivity_analyzer
        
        fert_sensitivity_res = wheat_sensitivity_module.analyze_input_cost_sensitivity('fertilizer_total', 10)
        print("\nSensitivity to +10% Fertilizer Cost (Wheat):")
        print(f"  New Net Margin: ${fert_sensitivity_res.get('new_net_margin_usd_ha', 'N/A'):.2f}/ha (Change: ${fert_sensitivity_res.get('change_net_margin_usd_ha', 'N/A'):.2f}/ha)")

        fuel_sensitivity_res = wheat_sensitivity_module.analyze_input_cost_sensitivity('fuel_machinery_ops', -15)
        print("Sensitivity to -15% Fuel Cost (Wheat):")
        print(f"  New Net Margin: ${fuel_sensitivity_res.get('new_net_margin_usd_ha', 'N/A'):.2f}/ha (Change: ${fuel_sensitivity_res.get('change_net_margin_usd_ha', 'N/A'):.2f}/ha)")

        price_sensitivity_res = wheat_sensitivity_module.analyze_price_sensitivity(8)
        print("Sensitivity to +8% Market Price (Wheat):")
        print(f"  New Net Margin: ${price_sensitivity_res.get('new_net_margin_usd_ha', 'N/A'):.2f}/ha (Change: ${price_sensitivity_res.get('change_net_margin_usd_ha', 'N/A'):.2f}/ha)")
    else:
        print("Error: Wheat FarmMarginModel or SensitivityAnalyzer not initialized for detailed tests.")

    print("\n--- Section 6: Combined Input Cost Scenario (CORN Example via Orchestrator) ---")
    # This will set up a new farm model for corn internally and run sensitivity
    combined_corn_scenario_res = dynamics_orchestrator.simulate_input_price_scenario(
        crop_name="corn_grain", 
        fertilizer_changes={'total_impact_percent': 15}, 
        energy_changes={'diesel': 20}, # This will affect 'fuel_machinery_ops' in the temp farm model
        labour_changes={'field_worker_percent_change': 10}, # Affects 'labor' in temp farm model
        commodity_price_change_percent=-5
    )
    # The simulate_input_price_scenario method already prints its summary

    print("\n--------- Simulation Complete ---------") 