import sys
import os
import json
from io import StringIO

# Add project root to Python path to allow imports from modules
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
sys.path.insert(0, project_root)

# Import main classes from each module
# Note: Some modules might not have a runnable __main__ block or a single orchestrating class.
# We will focus on those that do, based on previous analysis.

from industry_transformation_landscape.geopolitical_disruption_supply_chain import GeopoliticalDisruptionSupplyChain
from industry_transformation_landscape.input_cost_dynamics_margin_structure import InputCostDynamicsMarginStructure, InputCostSensitivityAnalysis
from industry_transformation_landscape.trade_flow_reconfiguration_market_access import TradeFlowReconfigurationMarketAccess
# ClimateShockYieldVolatility does not have a __main__ block, assumed to be used by other modules or directly.

from value_chain_reconfiguration.production_system_transformation import ProductionSystemTransformation

from consulting_marketplace_evolution.client_need_transformation import ClientNeedTransformation
# ConsultingServicePortfolioEvolution does not have a __main__ block.
from consulting_marketplace_evolution.competitive_landscape_reshaping import CompetitiveLandscapeReshaping
from consulting_marketplace_evolution.talent_capability_requirements import TalentCapabilityRequirements

# Helper to capture print statements
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

def run_all_simulations():
    """
    Runs the main simulation examples from each module and collects their output.
    """
    results = {}

    print("--- Running GeopoliticalDisruptionSupplyChain Simulation ---")
    geo_disruption_sim = GeopoliticalDisruptionSupplyChain()
    with Capturing() as geo_output:
        print("--- Example: Chokepoint Disruption (Suez Canal) ---")
        suez_impact = geo_disruption_sim.run_chokepoint_disruption_scenario(
            chokepoint_name="Suez Canal",
            disruption_type="Blockage", 
            duration_weeks=4, # 30 days ~ 4 weeks
            affected_commodities=["grains", "oilseeds"] 
        )
        print(f"Simulated Suez Disruption Impact (4 weeks): {json.dumps(suez_impact, indent=2)}")

        print("\n--- Example: Conflict Impact (Ukraine) ---")
        ukraine_impact = geo_disruption_sim.run_conflict_impact_scenario(
            region_name="Ukraine/Black Sea Region", 
            conflict_intensity="High", 
            duration_months=12,
            affected_commodities=["Wheat", "Corn"] 
        )
        print(f"Simulated Ukraine Conflict Impact (Wheat, 12 months): {json.dumps(ukraine_impact, indent=2)}")

        print("\n--- Example: Trade Policy Impact (Export Ban) ---")
        ban_impact = geo_disruption_sim.run_trade_policy_scenario(
            commodity="Wheat",
            restricting_country="Major Exporter X", 
            policy_type="export_ban", 
            duration_months=3 
        )
        print(f"Simulated Export Ban Impact: {json.dumps(ban_impact, indent=2)}")

        print("\n--- Example: Geopolitical Risk Index Update ---")
        risk_index_result = geo_disruption_sim.update_geopolitical_risk_index()
        print(f"Geopolitical Risk Index: {json.dumps(risk_index_result, indent=2)}")

        print("\n--- Example: Supply Chain Diversification Analysis (Wheat) ---")
        diversification_result_wheat = geo_disruption_sim.analyze_supply_chain_diversification(commodity='wheat', risk_threshold='Medium')
        print(f"Wheat Diversification Analysis: {json.dumps(diversification_result_wheat, indent=2)}")
        
        print("\n--- Example: Supply Chain Diversification Analysis (Corn) ---")
        diversification_result_corn = geo_disruption_sim.analyze_supply_chain_diversification(commodity='corn', risk_threshold='Low') # Example with different params
        print(f"Corn Diversification Analysis: {json.dumps(diversification_result_corn, indent=2)}")

    results['GeopoliticalDisruptionSupplyChain'] = geo_output
    print("--- GeopoliticalDisruptionSupplyChain Simulation Complete ---")

    print("\n--- Running InputCostDynamicsMarginStructure Simulation ---")
    input_cost_sim = InputCostDynamicsMarginStructure()
    with Capturing() as input_cost_output:
        # Example from input_cost_dynamics_margin_structure.py
        print("\n--- Fertilizer Cost Impact Analysis ---")
        fertilizer_price_changes = {"Urea": 10, "DAP": 15}
        fertilizer_impact = input_cost_sim.fertilizer_model.simulate_price_impact_on_farm_costs(
            crop="corn_grain",  # Assuming 'corn_grain' is a valid key in FertilizerCostImpact's data
            percentage_change_urea=fertilizer_price_changes.get("Urea", 0),
            percentage_change_dap=fertilizer_price_changes.get("DAP", 0),
            percentage_change_potash=fertilizer_price_changes.get("Potash", 0) # Ensure all relevant types are handled
        )
        print(json.dumps(fertilizer_impact, indent=2))

        print("\n--- Energy Cost Analysis ---")
        energy_price_changes = {"Diesel": 20, "Electricity": 10}
        energy_impact = input_cost_sim.energy_model.analyze_price_change_impact(
            farm_type="Midwest US Grain Farm", 
            area_ha=100, # Defaulting area_ha, adjust if more specific info is available or needed
            percentage_change_diesel=energy_price_changes.get("Diesel", 0),
            percentage_change_electricity=energy_price_changes.get("Electricity", 0),
            percentage_change_natural_gas=energy_price_changes.get("Natural Gas", 0)
        )
        results["energy_cost_analysis"] = energy_impact
        print(f"Energy Cost Analysis Result: {json.dumps(energy_impact, indent=2)}")

        print("\n--- Labour Cost Dynamics ---")
        labour_wage_impact_result = input_cost_sim.labour_model.analyze_wage_rate_impact(
            crop_profile_key='corn_midwest_efficient', # ensure this key exists in LabourCostDynamics
            wage_key='general_farm_labour_usd_hr', # ensure this key exists
            percent_increase=15  # Example: 15% increase
        )
        results["labour_cost_dynamics"] = labour_wage_impact_result
        print(f"Labour Cost Dynamics Result: {json.dumps(labour_wage_impact_result, indent=2)}")
        
        print("\n--- Agri Input Price Index ---")
        if hasattr(input_cost_sim, 'price_index_model') and input_cost_sim.price_index_model:
            price_scenario_data = {'Fertilizers': 1.10, 'Energy': 1.05, 'Seeds': 1.02, 'Chemicals': 1.08, 'Labour': 1.03} # Factors
            
            # Reset to baseline before applying new scenario updates
            input_cost_sim.price_index_model.reset_to_baseline()

            for component, factor in price_scenario_data.items():
                # The component names in AgriInputPriceIndex are:
                # 'Fertilizers', 'Pesticides', 'Herbicides', 'Seeds', 'Fuel_Machinery', 'Labour', 'Utilities'
                # We need to map our scenario data or use the exact names.
                # For now, let's assume a direct mapping for components present in price_scenario_data
                # and that the 'factor' is the new index value (e.g., 110 for 10% increase if baseline is 100).
                # The update_component_price expects the new index value directly.
                
                # Let's use a more robust mapping or ensure keys match AgriInputPriceIndex internal component names
                # Current AgriInputPriceIndex components (from its __init__):
                # self.component_prices = {"Fertilizers": 100, "Pesticides": 100, ...}
                # So, factor * 100 is correct if factor 1.10 means new index 110.

                mapped_component = component # Default direct mapping
                if component == "Energy": # Example mapping
                    mapped_component = "Fuel_Machinery"
                elif component == "Chemicals": # Example mapping for "Chemicals"
                    # AgriInputPriceIndex has "Pesticides", "Herbicides". We might need to split this or have a general "Chemicals".
                    # For now, let's assume "Chemicals" maps to "Pesticides" for simplicity or that the model handles a general "Chemicals".
                    # Let's check component_weights keys from the model instance
                    pass # Keep 'Chemicals' if it's a valid key, or handle appropriately

                if mapped_component in input_cost_sim.price_index_model.component_weights:
                    input_cost_sim.price_index_model.update_component_price(mapped_component, factor * 100)
                elif component in input_cost_sim.price_index_model.component_weights: # Try original name if mapped didn't work
                     input_cost_sim.price_index_model.update_component_price(component, factor * 100)
                else:
                    print(f"Warning: Component '{component}' (mapped to '{mapped_component}') not found in price_index_model.component_weights. Skipping update for this component.")

            index_result = input_cost_sim.price_index_model._calculate_index() # Calling protected method as per original main
            results["agri_input_price_index"] = {"index_value": index_result, "scenario_data_applied": price_scenario_data}
            print(f"Simulated Agri Input Price Index: {index_result} based on scenario: {price_scenario_data}")
            
            # The call to get_index_component_details was problematic as the method doesn't exist.
            # If we want component details, we'd typically look at self.price_index_model.component_prices
            # or self.price_index_model.component_weights after updates.
            current_component_prices = input_cost_sim.price_index_model.component_prices
            results["agri_input_price_index_components"] = current_component_prices
            print(f"Agri Input Price Index Component Prices after update: {json.dumps(current_component_prices, indent=2)}")

        else:
            print("AgriInputPriceIndex model not available or not named 'price_index_model'. Skipping Agri Input Price Index.")
            results["agri_input_price_index"] = "Skipped"
            results["agri_input_price_index_components"] = "Skipped"

        print("\n--- Farm Margin Model ---")
        raw_fixed_costs = {
            "land_rent_or_ownership": 150.0,
            "machinery_depreciation": 100.0,
            "insurance_admin": 50.0
        }
        farm_financials_for_setup = {
            "crop_name": "Corn",
            "expected_yield": 10.0,  # t/ha
            "market_price": 200.0,  # USD/t
            "variable_costs": {  # This is 'variable_costs'
                "fertilizer_total": 250.0, # Placeholder, ideally from fertilizer_model output
                "energy_total": 150.0,     # Placeholder, ideally from energy_model output
                "labour_total": 100.0,     # Placeholder, ideally from labour_model output
                "seed": 120.0,
                "pesticides": 80.0,
                "other_variable": 50.0
            },
            "fixed_costs": sum(raw_fixed_costs.values()) # Summing the fixed costs dictionary
        }
        specific_farm_margin_model = input_cost_sim.setup_farm_scenario(**farm_financials_for_setup)
        margin_analysis = specific_farm_margin_model.get_full_margin_analysis()
        print(json.dumps(margin_analysis, indent=2))

        print("\n--- Input Cost Sensitivity Analysis ---")
        specific_sensitivity_analyzer = InputCostSensitivityAnalysis(farm_margin_model=specific_farm_margin_model)
        
        sensitivity_results = specific_sensitivity_analyzer.analyze_input_cost_sensitivity(
            cost_component_key="fertilizer",
            percentage_change=10
        )
        print(json.dumps(sensitivity_results, indent=2))

        print("\n--- Aggregate Scenario ---")
        aggregate_params_for_sim = {
            "fertilizer_changes": {"urea_percent_change": 15, "potash_percent_change": -5}, 
            "energy_changes": {"diesel_percent_change": 25}, 
            "labour_changes": {"wage_percent_change": 3}, 
            "commodity_price_change_percent": -10 # simulate_input_price_scenario takes this directly
        }
        full_impact = input_cost_sim.simulate_input_price_scenario(
            crop_name="wheat_grain", # Matches the crop from farm_financials setup
            fertilizer_changes=aggregate_params_for_sim["fertilizer_changes"],
            energy_changes=aggregate_params_for_sim["energy_changes"],
            labour_changes=aggregate_params_for_sim["labour_changes"],
            commodity_price_change_percent=aggregate_params_for_sim["commodity_price_change_percent"]
        )
        print(json.dumps(full_impact, indent=2))
    results['InputCostDynamicsMarginStructure'] = input_cost_output
    print("--- InputCostDynamicsMarginStructure Simulation Complete ---")

    print("\n--- Running TradeFlowReconfigurationMarketAccess Simulation ---")
    trade_flow_sim = TradeFlowReconfigurationMarketAccess()
    with Capturing() as trade_flow_output:
        # Example from trade_flow_reconfiguration_market_access.py
        print("\n--- Example 1: Market Access Analysis ---")
        market_access_result = trade_flow_sim.market_analyzer.analyze_market_access(
            commodity="Corn",
            exporting_country="US",
            importing_country="China",
            fob_price_usd_mt=250,
            volume_mt=1000000,
            product_attributes={"pesticide_residues": {"pesticide_x": 0.003}},
            trade_agreement_context="USMCA",
            product_origin_details={"regional_value_content_percent": 70}
        )
        results["market_access_analysis"] = market_access_result
        # Custom print for this complex dictionary to avoid overly long lines
        print(f"Market Access for Corn (US to China):")
        for key, value in market_access_result.items():
            if isinstance(value, dict):
                print(f"  {key}: {{...}}") # Summarize dicts for brevity in console
            else:
                print(f"  {key}: {value}")
        
        print("\n--- Example 2: Bilateral Relationship Evolution ---")
        us_china_details = trade_flow_sim.bilateral_evolution.get_relationship_details("US-China")
        results["us_china_relationship_details"] = us_china_details
        print(f"US-China Relationship Details: {json.dumps(us_china_details, indent=2)}")
        
        us_china_impact = trade_flow_sim.bilateral_evolution.model_impact(
            country_pair_key="US-China", 
            scenario_type="negative", 
            specific_event="Hypothetical soybean trade disruption due to policy change", 
            magnitude_factor=1.2 
        )
        results["us_china_negative_scenario_impact"] = us_china_impact
        print(f"US-China Negative Scenario Impact: {json.dumps(us_china_impact, indent=2)}")

        print("\n--- Example 3: New Barrier Development ---")
        barrier_sim_result = trade_flow_sim.barrier_developer.simulate_new_barrier(
            region="EU", 
            commodity="Beef", 
            barrier_type_key="SPS Measure", 
            trigger_event="New animal disease concern"
        )
        results["new_barrier_simulation"] = barrier_sim_result
        print(f"Simulated New SPS Barrier on Beef (EU): {json.dumps(barrier_sim_result, indent=2)}")

        print("\n--- Example 4: Trade Agreement Impact ---")
        cptpp_details = trade_flow_sim.agreement_analyzer.get_agreement_details("CPTPP")
        results["cptpp_agreement_details"] = cptpp_details
        print(f"CPTPP Agreement Details: {json.dumps(cptpp_details, indent=2)}")
        
        cptpp_impact_analysis = trade_flow_sim.agreement_analyzer.analyze_impact_on_commodity_flow(
            agreement_name="CPTPP",
            commodity="Dairy",
            exporting_country="New Zealand",
            importing_country="Canada"
        )
        results["cptpp_impact_analysis"] = cptpp_impact_analysis
        print(f"CPTPP Impact on Dairy (NZ to Canada): {json.dumps(cptpp_impact_analysis, indent=2)}")

    results['TradeFlowReconfigurationMarketAccess'] = trade_flow_output
    print("--- TradeFlowReconfigurationMarketAccess Simulation Complete ---")

    print("\n--- Running ProductionSystemTransformation Simulation ---")
    prod_sys_sim = ProductionSystemTransformation()
    with Capturing() as prod_sys_output:
        # Example from production_system_transformation.py
        # The run_scenario method expects: region, years_to_project, consolidation_driver_factor (optional)
        prod_sys_scenario_params = {
            "region": "Global", # Original script used "Global"
            "years_to_project": 10 # Original script used 10 for time_horizon_years
            # "consolidation_driver_factor": 1.0 # Default, can be added if specific value needed
        }
        print(f"Running ProductionSystemTransformation scenario with params: {prod_sys_scenario_params}")
        results_scenario = prod_sys_sim.run_scenario(**prod_sys_scenario_params)
        results["production_system_transformation_scenario"] = results_scenario
        # The run_scenario method itself prints a lot of details.
        # We can print a summary or selected parts of results_scenario if needed.
        print(f"Production System Transformation Scenario completed for {prod_sys_scenario_params['region']}.")
        if 'consolidation_projection' in results_scenario and results_scenario['consolidation_projection']:
            print(f"  Consolidation Projection for {results_scenario['consolidation_projection'].get('region', 'N/A')}: ")
            print(f"    Projected Avg Farm Size: {results_scenario['consolidation_projection'].get('projected_avg_ha_in_years', 'N/A')} ha")

    results['ProductionSystemTransformation'] = prod_sys_output
    print("--- ProductionSystemTransformation Simulation Complete ---")

    print("\n--- Running ClientNeedTransformation Simulation ---")
    client_need_sim = ClientNeedTransformation()
    with Capturing() as client_need_output:
        # Example from client_need_transformation.py
        print("--- Client Priority Evolution ---")
        climate_priority_details = client_need_sim.priority_evolution.model_evolution(
            priority_area="Climate Risk Assessment and Mitigation"
            # years_to_project defaults to 5, can be specified if needed
        )
        print(f"Climate Priority Details & 5yr Projection: {json.dumps(climate_priority_details, indent=2)}")
        
        # Corrected method call: project_future_importance -> model_evolution
        supply_chain_resilience_projection = client_need_sim.priority_evolution.model_evolution(
            priority_area="Supply Chain Resilience Enhancement", # Ensuring exact name from class
            years_to_project=5
        )
        results["client_priority_supply_chain_resilience_projection"] = supply_chain_resilience_projection
        print(f"Supply Chain Resilience Projection (5 yrs): {json.dumps(supply_chain_resilience_projection, indent=2)}")

        print("\n--- Decision Maker Profile Shift ---")
        cso_profile = client_need_sim.decision_maker_shift.get_profile("Chief Sustainability Officer (CSO)")
        results["decision_maker_cso_profile"] = cso_profile
        print(f"CSO Profile: {json.dumps(cso_profile, indent=2)}")

        print("\n--- Problem Framing Evolution ---")
        sustainability_framing = client_need_sim.problem_framing_evolution.get_framing_details("Sustainability & ESG Integration")
        print(f"Sustainability Framing: {json.dumps(sustainability_framing, indent=2)}")
        
        print("\n--- Budget Allocation Shifts ---")
        digital_budget = client_need_sim.budget_allocation_shifts.get_allocation_details("Digital Transformation & AgTech")
        results["budget_allocation_digital"] = digital_budget
        print(f"Digital Transformation Budget Details: {json.dumps(digital_budget, indent=2)}")
        
        print("\n--- Sector Boundary Blurring ---")
        tech_blur_implications = client_need_sim.sector_boundary_blurring.analyze_implications_for_client(
            blurring_example_name="Tech Companies in Agriculture", 
            client_type="Traditional Agribusinesses"
        )
        results["sector_blurring_tech_implications"] = tech_blur_implications
        print(f"Tech Blurring Implications for Agribusiness: {json.dumps(tech_blur_implications, indent=2)}")

        print("\n--- Overall Client Needs Simulation ---")
        sim_results = client_need_sim.get_comprehensive_client_outlook(
            client_segment="Large Diversified Agribusiness",
            region="Global" 
        )
        results["comprehensive_client_outlook"] = sim_results
        print(json.dumps(sim_results, indent=2))
    results['ClientNeedTransformation'] = client_need_output
    print("--- ClientNeedTransformation Simulation Complete ---")

    print("\n--- Running CompetitiveLandscapeReshaping Simulation ---")
    comp_landscape_sim = CompetitiveLandscapeReshaping()
    with Capturing() as comp_landscape_output:
        # Example from competitive_landscape_reshaping.py
        print("--- Strategy Consulting Firm Positioning ---")
        bcg_profile = comp_landscape_sim.strategy_positioning.get_firm_positioning_details("Global Strategy Leader (e.g., BCG, McKinsey)")
        results["strategy_firm_bcg_profile"] = bcg_profile
        print(json.dumps(bcg_profile, indent=2))

        print("\n--- Market Intelligence Provider Evolution ---")
        specialized_mi = comp_landscape_sim.market_intelligence_evolution.get_provider_type_details("Specialized Agri-focused MI & Advisory (e.g., Gro Intelligence, IHS Markit Agribusiness)")
        print(json.dumps(specialized_mi, indent=2))

        print("\n--- Technical Advisory Transformation ---")
        sustainability_advisory = comp_landscape_sim.technical_advisory_transformation.get_service_area_details("Sustainability & Environmental Compliance")
        print(json.dumps(sustainability_advisory, indent=2))

        print("\n--- Specialist Boutique Emergence ---")
        agtech_boutique = comp_landscape_sim.specialist_boutiques.get_boutique_profile("AgTech Strategy & Implementation Boutique")
        print(json.dumps(agtech_boutique, indent=2))

        print("\n--- New Entrant Threat Assessment ---")
        tech_entrant_threat = comp_landscape_sim.new_entrants_assessment.assess_threat_to_traditional_model(
            entrant_type_name="Technology & Data Analytics Firms (e.g., ClimateAI, EOS Data Analytics)"
        )
        results["new_entrant_tech_threat"] = tech_entrant_threat
        print(json.dumps(tech_entrant_threat, indent=2))

        print("\n--- Comprehensive Landscape Analysis ---")
        print("Skipping non-existent 'get_overall_landscape_snapshot'. Individual analyses are already performed.")

    results['CompetitiveLandscapeReshaping'] = comp_landscape_output
    print("--- CompetitiveLandscapeReshaping Simulation Complete ---")

    print("\n--- Running TalentCapabilityRequirements Simulation ---")
    talent_sim = TalentCapabilityRequirements()
    with Capturing() as talent_output:
        # Example from talent_capability_requirements.py
        print("--- Consultant Skill Profile Evolution ---")
        future_profile = talent_sim.skill_evolution.get_skill_profile(
            profile_name="Future-State Agricultural Consultant (Next 5-10 Years)"
        )
        results["talent_future_skill_profile"] = future_profile
        print(json.dumps(future_profile, indent=2))
        
        skill_gap_analysis = talent_sim.skill_evolution.identify_skill_gaps(
            current_profile_name="Emerging Agricultural Consultant (Current State)",
            target_profile_name="Future-State Agricultural Consultant (Next 5-10 Years)"
        )
        print(json.dumps(skill_gap_analysis, indent=2))

        print("\n--- Talent Acquisition Strategy ---")
        # Corrected method call: get_strategy_for_role -> develop_strategy
        # develop_strategy does not take arguments in the current implementation.
        data_scientist_strategy = talent_sim.acquisition_strategy.develop_strategy() 
        results["talent_acquisition_strategy_generic"] = data_scientist_strategy
        print(json.dumps(data_scientist_strategy, indent=2))

        print("\n--- Training and Development Program ---")
        # Corrected method call: get_program_details -> design_program
        # design_program does not take arguments in the current implementation.
        sustainability_training = talent_sim.training_programs.design_program()
        results["talent_training_program_generic"] = sustainability_training
        print(json.dumps(sustainability_training, indent=2))

        print("\n--- Organizational Structure Adaptation ---")
        # Corrected attribute: org_structure_adaptation -> culture_adaptation
        # Corrected method: get_structure_details -> recommend_changes
        # recommend_changes does not take arguments in the current implementation.
        matrix_structure_or_culture_recs = talent_sim.culture_adaptation.recommend_changes()
        results["talent_org_culture_recommendations"] = matrix_structure_or_culture_recs
        print(json.dumps(matrix_structure_or_culture_recs, indent=2))

        print("\n--- Full Talent Landscape Simulation ---")
        # Corrected method name: simulate_talent_landscape_changes -> run_talent_analysis_scenario
        # Adjusted parameters to match the actual method definition.
        full_talent_analysis = talent_sim.run_talent_analysis_scenario(
            scenario_name="RunSimulationPyTalentScenario" # consulting_firm_type and years_projection are not used by this method
        )
        results["talent_full_landscape_analysis"] = full_talent_analysis
        print(json.dumps(full_talent_analysis, indent=2))

    results['TalentCapabilityRequirements'] = talent_output
    print("--- TalentCapabilityRequirements Simulation Complete ---")

    return results

def generate_html_report(simulation_results, output_file="simulation_report.html"):
    """
    Generates an HTML report from the simulation results.
    """
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agricultural Commodities Consulting Simulation Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; line-height: 1.6; background-color: #f4f4f4; color: #333; }
        .container { background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
        h2 { color: #3498db; margin-top: 30px; border-bottom: 1px solid #e0e0e0; padding-bottom: 5px;}
        h3 { color: #2980b9; margin-top: 20px; }
        pre { background-color: #ecf0f1; padding: 15px; border-radius: 5px; overflow-x: auto; border: 1px solid #bdc3c7; white-space: pre-wrap; word-wrap: break-word; }
        .module-section { margin-bottom: 30px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;}
        .timestamp { font-size: 0.9em; color: #7f8c8d; text-align: right; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Agricultural Commodities Consulting - Simulation Report</h1>
        <p class="timestamp">Generated on: <span id="datetime"></span></p>
        <script>
            document.getElementById('datetime').textContent = new Date().toLocaleString();
        </script>
"""

    for module_name, output_lines in simulation_results.items():
        html_content += f"<div class='module-section'>\\n"
        html_content += f"<h2>{module_name.replace('_', ' ').title()}</h2>\\n"
        # Attempt to parse JSON if possible for better formatting, otherwise preformat
        current_block = ""
        for line in output_lines:
            current_block += line + "\\n"
        
        # Check if the block is likely JSON
        # Simple check: starts with { or [ and ends with } or ] after stripping
        stripped_block = current_block.strip()
        if (stripped_block.startswith('{') and stripped_block.endswith('}')) or \
           (stripped_block.startswith('[') and stripped_block.endswith(']')):
            try:
                # Try to parse and re-serialize with indentation for pretty printing
                json_obj = json.loads(stripped_block)
                html_content += f"<pre>{json.dumps(json_obj, indent=2)}</pre>\\n"
            except json.JSONDecodeError:
                # Not valid JSON, or complex structure not simply parsed
                html_content += f"<pre>{current_block}</pre>\\n" # Fallback
        else:
             html_content += f"<pre>{current_block}</pre>\\n"
        html_content += "</div>\\n"

    html_content += """
    </div>
</body>
</html>
"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"\\nHTML report generated: {output_file}")

if __name__ == "__main__":
    print("Starting all simulations...")
    all_results = run_all_simulations()
    print("\\nAll simulations complete.")
    
    print("\\nGenerating HTML report...")
    generate_html_report(all_results)
    
    print("\\nProcess finished.")
    print(f"Report available at: {os.path.join(project_root, 'simulation_report.html')}") 