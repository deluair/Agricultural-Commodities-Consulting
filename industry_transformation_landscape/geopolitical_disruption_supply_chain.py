# This module will handle simulations related to Geopolitical Disruption & Supply Chain Vulnerability.

class ShippingChokepointVulnerability:
    """
    Models the vulnerability of key maritime shipping chokepoints to various disruptions
    and estimates the potential impact on agricultural commodity trade.
    """
    def __init__(self):
        self.chokepoints_data = {
            "Suez Canal": {
                "description": "Connects Mediterranean Sea to Red Sea/Indian Ocean. Vital for East-West trade.",
                "commodities_handled": ["grains (wheat, corn)", "oilseeds", "fertilizers", "general cargo"],
                "vulnerabilities": ["blockages (e.g., Ever Given)", "geopolitical tensions in Red Sea/Middle East", 
                                  "climate (high winds, dust storms, sea level rise affecting canal infrastructure)"],
                "typical_daily_trade_value_usd_billion": 9.6, # Estimate from Ever Given incident
                "annual_grain_trade_percent_global": 15 # Approximate
            },
            "Panama Canal": {
                "description": "Connects Atlantic and Pacific Oceans. Key for Americas-Asia trade.",
                "commodities_handled": ["soybeans", "grains", "corn", "cotton", "fruits", "vegetables"],
                "vulnerabilities": ["climate (low water levels due to drought/El Niño, impacting vessel draft/capacity)",
                                  "lock malfunctions", "congestion"],
                "notes": "Droughts in 2016, 1997-98, and 2023-24 significantly impacted transit."
            },
            "Turkish Straits (Bosporus & Dardanelles)": {
                "description": "Connects Black Sea to Mediterranean. Critical for Black Sea agricultural exports.",
                "commodities_handled": ["wheat", "barley", "corn", "sunflower oil/seeds", "rapeseed"],
                "vulnerabilities": ["geopolitical tensions (e.g., Russia-Ukraine conflict, regional instability)",
                                  "congestion", "accidents", "weather (fog, storms)", "political decisions (Montreux Convention)"],
                "notes": "Russia & Ukraine account for significant global shares of wheat, barley, sunflower oil."
            },
            "Strait of Hormuz": {
                "description": "Connects Persian Gulf to Gulf of Oman/Arabian Sea. Primarily oil, but also fertilizers.",
                "commodities_handled": ["oil/LNG", "fertilizers (urea, ammonia)"],
                "vulnerabilities": ["geopolitical tensions in the Middle East", "military conflict", "piracy/attacks"],
            },
            "Strait of Malacca": {
                "description": "Connects Indian Ocean to South China Sea/Pacific. Major global trade route.",
                "commodities_handled": ["palm oil", "rice", "rubber", "general cargo", "oil"],
                "vulnerabilities": ["piracy", "congestion", "accidents", "natural disasters (tsunamis)"],
            },
            "Strait of Bab-al-Mandab": {
                "description": "Connects Red Sea to Gulf of Aden/Indian Ocean. Linked with Suez Canal traffic.",
                "commodities_handled": ["similar to Suez Canal traffic"],
                "vulnerabilities": ["geopolitical tensions (Yemen conflict)", "piracy/attacks"],
            }
        }

    def model_vulnerability(self, chokepoint_name: str, disruption_scenario: str, duration_days: int, affected_commodities: list = None):
        """
        Model shipping chokepoint vulnerability based on a disruption scenario.

        Args:
            chokepoint_name (str): Name of the chokepoint (e.g., "Suez Canal", "Panama Canal").
            disruption_scenario (str): Description of the disruption (e.g., "total_blockage", 
                                       "reduced_capacity_50_percent", "conflict_closure", "climate_event_low_water").
            duration_days (int): Duration of the disruption in days.
            affected_commodities (list, optional): Specific commodities to focus on. Defaults to all key commodities for the chokepoint.

        Returns:
            dict: An assessment of the vulnerability and potential impacts.
                  Example: {
                      'chokepoint': 'Suez Canal',
                      'scenario': 'total_blockage',
                      'duration_days': 6,
                      'estimated_trade_disrupted_usd': 57.6e9,
                      'key_commodities_at_risk': ['grains', 'oilseeds'],
                      'potential_impacts': [
                          'Increased shipping times and costs due to re-routing (e.g., around Cape of Good Hope)',
                          'Port congestion at alternative hubs',
                          'Supply chain delays for dependent regions',
                          'Price volatility for affected commodities',
                          'Food security concerns for highly import-dependent nations.'
                      ],
                      'notes': 'Based on Ever Given type incident.'
                  }
        """
        if chokepoint_name not in self.chokepoints_data:
            return {"error": f"Chokepoint {chokepoint_name} not found in database."}

        data = self.chokepoints_data[chokepoint_name]
        impact_assessment = {
            'chokepoint': chokepoint_name,
            'description': data.get('description'),
            'scenario': disruption_scenario,
            'duration_days': duration_days,
            'known_vulnerabilities': data.get('vulnerabilities'),
            'key_commodities_handled': data.get('commodities_handled'),
            'estimated_trade_disrupted_usd': None,
            'commodities_focused_on': affected_commodities if affected_commodities else data.get('commodities_handled'),
            'potential_impacts': [],
            'mitigation_considerations': ['Re-routing options (if available)', 'Alternative sourcing', 
                                          'Drawing down stockpiles', 'Diplomatic efforts (for political disruptions)'],
            'notes': data.get('notes', '')
        }

        # Simplified impact estimation
        if chokepoint_name == "Suez Canal" and "blockage" in disruption_scenario:
            daily_trade_value = data.get('typical_daily_trade_value_usd_billion', 0) * 1e9
            impact_assessment['estimated_trade_disrupted_usd'] = daily_trade_value * duration_days
            impact_assessment['potential_impacts'].extend([
                f"Significant daily trade value disrupted (approx ${daily_trade_value/1e9:.1f}B/day).",
                "Re-routing around Cape of Good Hope: + ~10-14 days, increased fuel & emissions.",
                "Global container and bulk freight rates likely to spike.",
                f"{data.get('annual_grain_trade_percent_global')}% of global grain trade potentially affected if prolonged."
            ])
        elif chokepoint_name == "Panama Canal" and ("low_water" in disruption_scenario or "drought" in disruption_scenario):
            capacity_reduction_factor = 0.5 if "50_percent" in disruption_scenario else 0.3 # Default assumption for generic low water
            impact_assessment['potential_impacts'].extend([
                f"Reduced vessel draft and transit capacity by ~{capacity_reduction_factor*100:.0f}%.",
                "Longer queues and waiting times for transit.",
                "Increased cost per ton due to lighter loads or use of smaller vessels.",
                "Shift to alternative routes (e.g., Suez, US intermodal) if severe/prolonged, adding cost/time.",
                "Particular impact on US grain/soybean exports to Asia, and fruit/veg from West Coast LatAm to Europe/US East Coast."
            ])
            impact_assessment['notes'] += " Impact is highly dependent on actual water levels and restrictions imposed."
        elif chokepoint_name == "Turkish Straits" and ("conflict" in disruption_scenario or "closure" in disruption_scenario):
            impact_assessment['potential_impacts'].extend([
                "Severe disruption to Black Sea exports (wheat, corn, sunflower oil) from Ukraine, Russia, etc.",
                "Significant impact on global food security, especially for North Africa, Middle East, and other import-dependent nations.",
                "Sharp increase in global prices for affected commodities.",
                "Search for alternative suppliers (e.g., EU, Americas, Australia) leading to market shifts.",
                "Fertilizer supply chains could also be impacted."
            ])
            impact_assessment['notes'] += " Ukraine/Russia war demonstrated severe consequences of this disruption."
        else: # Generic impacts
            impact_assessment['potential_impacts'].append("Disruption to trade flows for key commodities handled.")
            impact_assessment['potential_impacts'].append("Potential for increased shipping costs and delays.")
            impact_assessment['potential_impacts'].append("Market uncertainty and price volatility for related commodities.")

        impact_assessment['potential_impacts'].append("Increased insurance premiums for vessels in affected areas.")
        impact_assessment['potential_impacts'].append("Downstream impacts on food processors and consumers.")
        
        # Refine commodities at risk based on input or all handled
        impact_assessment['specific_commodities_at_high_risk'] = affected_commodities if affected_commodities else data.get('commodities_handled', [])

        return impact_assessment

class ConflictZoneProduction:
    """
    Simulates the impact of conflicts in key agricultural production or import-dependent zones
    on production levels, trade flows, and food security.
    """

    def __init__(self):
        self.conflict_impact_data = {
            "Ukraine/Black Sea Region": {
                "key_exports": ["wheat", "corn", "barley", "sunflower oil", "rapeseed"],
                "global_export_share_approx": {
                    "wheat": 0.10, # Ukraine's share, Russia adds more
                    "corn": 0.15,
                    "sunflower_oil": 0.50 # Ukraine alone, Russia also significant
                },
                "impact_factors": [
                    "direct production loss (damaged land, machinery, labor shortages)",
                    "export infrastructure damage/blockade (ports, rail)",
                    "input shortages (fuel, fertilizer, seeds)",
                    "storage facility damage/loss",
                    "logistics disruption & increased costs"
                ],
                "dependent_regions": ["North Africa (Egypt, Tunisia, Libya)", "Middle East", "Sub-Saharan Africa", "Parts of Asia"],
                "historical_notes": "Russia-Ukraine war (2022 onwards) caused significant production/export drops, price spikes, and food security alerts. Black Sea Grain Initiative offered partial, intermittent relief."
            },
            "Sahel Region (Sub-Saharan Africa)": {
                "key_production": ["sorghum", "millet", "livestock"],
                "impact_factors": [
                    "displacement of farming populations",
                    "loss of livestock",
                    "disruption of pastoral routes",
                    "breakdown of local markets",
                    "restricted access for humanitarian aid",
                    "exacerbation by climate change (drought, desertification)"
                ],
                "dependent_regions": ["Local populations, regional trade within West Africa"],
                "historical_notes": "Numerous ongoing conflicts exacerbate food insecurity, leading to crisis levels in several areas."
            },
            "Middle East (e.g., Syria, Yemen)": {
                "key_imports": ["wheat", "rice", "barley", "poultry"],
                "production_systems_affected": ["local rain-fed agriculture", "irrigated farming (vulnerable to infrastructure damage)", "livestock"],
                "impact_factors": [
                    "destruction of agricultural infrastructure (irrigation, storage)",
                    "displacement of farmers",
                    "breakdown of supply chains for inputs and outputs",
                    "hyperinflation and currency devaluation impacting import capacity",
                    "blockades restricting food and aid imports (e.g., Yemen)",
                    "loss of income and purchasing power"
                ],
                "dependent_regions": ["Highly import-dependent populations within these conflict zones"],
                "historical_notes": "Prolonged conflicts have led to famine or near-famine conditions, severe malnutrition."
            }
            # Can add more regions/conflict types
        }

    def simulate_production_impact(self, region: str, conflict_intensity: str, duration_months: int, affected_crops: list = None):
        """
        Simulates the impact of conflict on agricultural production in a given region.

        Args:
            region (str): The conflict-affected region (e.g., "Ukraine/Black Sea Region", "Sahel Region").
            conflict_intensity (str): E.g., "low", "medium", "high", "active_warfare".
            duration_months (int): Duration of the conflict at this intensity.
            affected_crops (list, optional): Specific crops to focus on. Defaults to key crops of the region.

        Returns:
            dict: Estimated production impact.
                  Example: {
                      'region': 'Ukraine/Black Sea Region',
                      'conflict_intensity': 'high',
                      'duration_months': 12,
                      'estimated_production_loss_percent': {'wheat': 0.35, 'corn': 0.40},
                      'contributing_factors': ['port blockades', 'reduced planting area', 'input shortages'],
                      'notes': 'Significant disruption to planting, harvest, and export operations.'
                  }
        """
        if region not in self.conflict_impact_data:
            return {"error": f"Conflict impact data for region '{region}' not found."}

        regional_data = self.conflict_impact_data[region]
        crops_to_assess = affected_crops if affected_crops else regional_data.get("key_exports", regional_data.get("key_production", []))
        
        loss_percentage = {}
        intensity_multiplier = {"low": 0.1, "medium": 0.3, "high": 0.6, "active_warfare": 0.8}
        base_loss = intensity_multiplier.get(conflict_intensity, 0.4) # Default to medium-high if intensity not mapped

        for crop in crops_to_assess:
            # Simplified loss calculation: higher loss for higher intensity and longer duration (capped)
            # This is a placeholder for a more complex model
            crop_loss = min(base_loss * (1 + (duration_months / 12) * 0.5), 0.95) # Max 95% loss
            loss_percentage[crop] = round(crop_loss, 2)
        
        contributing_factors = regional_data.get("impact_factors", [])

        return {
            'region': region,
            'conflict_intensity': conflict_intensity,
            'duration_months': duration_months,
            'estimated_production_loss_percent': loss_percentage,
            'contributing_factors': contributing_factors,
            'dependent_regions_potentially_impacted': regional_data.get('dependent_regions', 'N/A'),
            'notes': f"Estimated impact based on specified intensity and duration. Actual impact varies greatly. {regional_data.get('historical_notes', '')}"
        }

    def estimate_food_security_implications(self, producing_region_scenario: dict, importing_region: str):
        """
        Estimates food security implications for an importing region based on production shocks
        in a key supplying region and its import dependency.

        Args:
            producing_region_scenario (dict): Output from simulate_production_impact.
            importing_region (str): Name of the importing region (e.g., "Egypt", "MENA_general", "Global Market").

        Returns:
            dict: Assessment of food security implications.
                  Example: {
                      'importing_region': 'Egypt',
                      'supplying_region_scenario': { ... },
                      'key_commodity_shortfall': 'wheat',
                      'estimated_price_increase_range_percent': (20, 50), # Placeholder
                      'vulnerability_factors': ['high import dependency on Black Sea wheat', 'bread subsidies strain budget'],
                      'potential_consequences': ['increased food import bill', 'domestic food price inflation',
                                               'social unrest risk', 'need for alternative suppliers/aid']
                  }
        """
        if 'error' in producing_region_scenario:
            return {"error": "Invalid producing_region_scenario provided.", "details": producing_region_scenario['error']}

        # Placeholder logic - this would require detailed trade data and economic models
        implications = {
            'importing_region': importing_region,
            'supplying_region_scenario': producing_region_scenario,
            'key_commodity_shortfall': [],
            'estimated_price_increase_range_percent': (10, 60), # Generic placeholder
            'vulnerability_factors': [],
            'potential_consequences': [
                "Increased cost of imported food.",
                "Potential shortages of specific commodities if alternative sourcing is difficult/expensive.",
                "Increased domestic food price inflation.",
                "Strain on household budgets, especially for low-income families.",
                "Government fiscal pressure due to subsidies or social safety net costs.",
                "Increased reliance on humanitarian aid for vulnerable populations."
            ],
            'mitigation_options_for_importer': [
                "Seek alternative import sources (diversification).",
                "Increase domestic production (if feasible, medium/long term).",
                "Implement/expand social safety nets.",
                "Request international aid/concessional finance.",
                "Draw down strategic reserves (if any).",
                "Consumer behavior changes (e.g., dietary substitution if possible)."
            ]
        }

        production_losses = producing_region_scenario.get('estimated_production_loss_percent', {})
        supplying_region = producing_region_scenario.get('region')
        key_exports_from_supplier = self.conflict_impact_data.get(supplying_region, {}).get('key_exports', [])

        for crop, loss in production_losses.items():
            if loss > 0.2 and crop in key_exports_from_supplier: # Arbitrary threshold for significant shortfall
                implications['key_commodity_shortfall'].append(crop)
        
        # Add region-specific vulnerabilities (examples)
        if importing_region == "Egypt" and supplying_region == "Ukraine/Black Sea Region":
            implications['vulnerability_factors'].extend([
                "High dependency on Black Sea wheat (historically ~80-85% from Russia/Ukraine).",
                "Wheat is a key staple (bread subsidies are significant fiscal item).",
                "Existing economic pressures (inflation, currency devaluation)."
            ])
            implications['estimated_price_increase_range_percent'] = (30, 70) # More specific placeholder
        elif importing_region.startswith("North Africa") and supplying_region == "Ukraine/Black Sea Region":
            implications['vulnerability_factors'].extend([
                "Structural reliance on cereal imports from Black Sea.",
                "Water scarcity limiting domestic production potential.",
                "Socio-economic fragility in some countries (e.g., Tunisia, Libya)."
            ])

        if not implications['key_commodity_shortfall']:
            implications['notes'] = "Assumed impact based on scenario, but specific commodity shortfall not high enough to flag or not a key export."
        
        return implications

class ExportRestrictionRisk:
    def track_proliferation_risk(self, policy_type: str):
        """
        Track export restriction proliferation risk.
        - Food nationalism policy trigger threshold identification
        - Export tax implementation probability modeling
        - License requirement introduction likelihood assessment
        - Quota system design prediction framework
        - WTO compliance strategy evolution
        """
        pass

class StockpilingBehaviorProjection:
    def project_behavior(self, economy_type: str):
        """
        Project stockpiling behavior by economy type.
        - Strategic reserve ratio target evolution by country
        - Import-dependent nation buffer stock policy patterns
        - Private sector inventory behavior under uncertainty
        - Public-private stock management coordination trends
        - Transparency regime development trajectory
        """
        pass

class TransportCostShockTransmission:
    def simulate_transmission(self, cost_type: str, shock_level: float):
        """
        Simulate transport cost shock transmission.
        - Bunker fuel price pass-through elasticity
        - Container availability constraint impact
        - Bulk freight rate volatility effect on landed cost
        - Port congestion cost quantification
        - Logistics bottleneck formation probability modeling
        """
        pass 

class TradePolicySanctionImpact:
    """
    Analyzes the impact of trade policies (export bans, tariffs, quotas) and sanctions
    on agricultural commodity flows and market stability.
    """

    def __init__(self):
        self.policy_types = {
            "export_ban": {
                "description": "Complete prohibition on exporting specific commodities.",
                "common_triggers": ["domestic food security crisis", "severe price inflation", "national emergency"],
                "typical_impacts": ["sharp global price increase", "domestic price decrease", "severe supply shock for importers"]
            },
            "export_quota": {
                "description": "Quantitative limit on the amount of a commodity that can be exported.",
                "common_triggers": ["manage domestic supply", "stabilize prices", "fulfill trade agreements"],
                "typical_impacts": ["moderate global price increase", "supply constraint", "potential for trade diversion"]
            },
            "export_tax": {
                "description": "Tax levied on exported goods.",
                "common_triggers": ["revenue generation", "discourage raw material export", "manage domestic prices"],
                "typical_impacts": ["increased cost for importers", "potential reduction in export volume", "domestic price stabilization"]
            },
            "import_tariff": {
                "description": "Tax levied on imported goods to protect domestic producers.",
                "common_triggers": ["protect domestic industry", "revenue generation", "address trade imbalances"],
                "typical_impacts": ["higher prices for consumers in importing country", "reduced import volumes", "potential trade tensions"]
            },
            "sanctions": {
                "description": "Economic penalties applied by one or more countries against a targeted country, group, or individual.",
                "common_triggers": ["geopolitical reasons", "human rights violations", "security concerns"],
                "typical_impacts": ["disruption of financial transactions", "restriction on specific goods/services", "broader economic hardship for targeted entity"]
            }
        }
        self.historical_examples = [
            {"policy_type": "export_ban", "commodity": "rice", "country": "India", "year": 2023, "reason": "domestic food security", "impact_summary": "Global rice price surge, concerns for African importers."},
            {"policy_type": "export_ban", "commodity": "palm_oil", "country": "Indonesia", "year": 2022, "reason": "domestic cooking oil shortage", "impact_summary": "Global vegetable oil market volatility."},
            {"policy_type": "export_tax", "commodity": "wheat", "country": "Russia", "year": "ongoing", "reason": "stabilize domestic market, revenue", "impact_summary": "Increased cost for importers, affects global wheat prices."},
            {"policy_type": "sanctions", "commodity": "various", "country": "Russia", "year": "2022-present", "reason": "Ukraine conflict", "impact_summary": "Disruption to grain and fertilizer exports, payment difficulties, increased shipping costs."}
        ]

    def simulate_export_restriction_impact(self, commodity, restricting_country, policy_type, restriction_level_percent=None, duration_months=None):
        """
        Simulates the market impact of a specific export restriction.

        Args:
            commodity (str): The affected commodity (e.g., 'wheat', 'rice').
            restricting_country (str): The country imposing the restriction.
            policy_type (str): Type of policy (e.g., 'export_ban', 'export_quota', 'export_tax').
            restriction_level_percent (float, optional): For quotas/taxes, the level of restriction.
                                                        e.g., for quota, % of normal exports allowed.
                                                        e.g., for tax, the tax rate as %.
            duration_months (int, optional): Estimated duration of the restriction.

        Returns:
            dict: A dictionary detailing the simulated impacts.
        """
        if policy_type not in self.policy_types:
            return {"error": "Invalid policy type specified."}

        policy_details = self.policy_types[policy_type]
        impact_assessment = {
            "scenario": f"{policy_type.replace('_', ' ').title()} on {commodity} by {restricting_country}",
            "assumed_restriction_level_percent": restriction_level_percent,
            "assumed_duration_months": duration_months,
            "potential_global_supply_reduction_percent": 0, # Placeholder
            "estimated_international_price_increase_percent": 0, # Placeholder
            "estimated_domestic_price_decrease_percent_in_restricting_country": 0, # Placeholder
            "key_affected_importing_regions": [], # Placeholder
            "trade_diversion_potential": "low/medium/high", # Placeholder
            "food_security_impact_level_in_dependent_nations": "low/medium/high" # Placeholder
        }

        # Simplified logic based on policy type
        if policy_type == "export_ban":
            impact_assessment["potential_global_supply_reduction_percent"] = "Significant (depends on exporter's market share)"
            impact_assessment["estimated_international_price_increase_percent"] = "High (e.g., 15-50%)"
            impact_assessment["estimated_domestic_price_decrease_percent_in_restricting_country"] = "Moderate (e.g., 5-20%)"
            impact_assessment["food_security_impact_level_in_dependent_nations"] = "High"
        elif policy_type == "export_quota":
            reduction = restriction_level_percent if restriction_level_percent is not None else 50 # Assume 50% reduction if not specified
            impact_assessment["potential_global_supply_reduction_percent"] = f"Moderate (proportional to quota, e.g., {reduction}% of typical exports from source)"
            impact_assessment["estimated_international_price_increase_percent"] = f"Moderate (e.g., 5-25%, depends on {reduction}%)"
            impact_assessment["food_security_impact_level_in_dependent_nations"] = "Medium"
        elif policy_type == "export_tax":
            impact_assessment["estimated_international_price_increase_percent"] = f"Low to Moderate (depends on tax rate {restriction_level_percent}%)"
            impact_assessment["food_security_impact_level_in_dependent_nations"] = "Low to Medium"

        # Placeholder for more sophisticated modeling
        # Actual impact would depend on commodity's global trade volume, restricting country's market share,
        # demand elasticity, availability of substitutes, inventories, etc.
        impact_assessment["notes"] = "This is a simplified qualitative assessment. Real impacts require detailed market modeling."
        impact_assessment["key_affected_importing_regions"] = ["To be determined based on commodity and exporter"]

        return impact_assessment

    def simulate_import_dependency_shock(self, importing_country, commodity, supplier_country, supply_reduction_percent, duration_months):
        """
        Simulates the shock to an importing country when a key supplier restricts exports.

        Args:
            importing_country (str): The country experiencing the shock.
            commodity (str): The commodity in question.
            supplier_country (str): The supplier country restricting exports.
            supply_reduction_percent (float): The percentage reduction in supply from that supplier.
            duration_months (int): The duration of the supply shock.

        Returns:
            dict: A dictionary detailing the simulated impacts on the importing country.
        """
        return {
            "scenario": f"Import shock for {importing_country} due to {supply_reduction_percent}% cut in {commodity} from {supplier_country}",
            "duration_months": duration_months,
            "direct_import_shortfall_volume": "Placeholder: Calculate based on typical imports",
            "estimated_domestic_price_hike_percent": "Placeholder: High, depends on import dependency share",
            "impact_on_food_security_index": "Placeholder: Negative impact score",
            "potential_alternative_suppliers": ["To be identified"],
            "coping_mechanisms": ["draw down reserves", "seek new suppliers", "reduce consumption", "request aid"],
            "vulnerability_score": "high/medium/low" # Based on dependency & commodity importance
        }

    def assess_market_response_strategies(self, disruption_event_details):
        """
        Assesses potential market response strategies by different actors to a trade policy disruption.

        Args:
            disruption_event_details (dict): Details of the disruption event from other simulation methods.

        Returns:
            dict: Potential responses by importers, exporters, and other market players.
        """
        return {
            "disruption_event": disruption_event_details,
            "responses_by_importers": [
                "Seek alternative sourcing (diversification)",
                "Negotiate new contracts (potentially at higher prices)",
                "Draw down strategic reserves (if available)",
                "Increase domestic production (long-term)",
                "Lobby for removal of restrictions",
                "Implement consumer rationing or subsidies"
            ],
            "responses_by_unaffected_exporters": [
                "Increase production/exports to fill supply gap (if possible)",
                "Target markets affected by restrictions",
                "Benefit from higher global prices"
            ],
            "responses_by_traders_speculators": [
                "Adjust positions based on price expectations",
                "Arbitrage opportunities if price differentials emerge",
                "Increased hedging activity"
            ],
            "responses_by_restricting_country_producers": [
                "Face lower domestic prices (potential income loss)",
                "May shift production if export ban is prolonged",
                "Lobby for policy reversal or compensation"
            ],
            "government_interventions_other_countries": [
                "Release strategic stocks",
                "Provide subsidies to consumers/importers",
                "Engage in diplomatic efforts to lift restrictions",
                "Consider retaliatory trade measures (risk escalation)"
            ]
        }

class GeopoliticalRiskIndex:
    """
    Develops a composite index to quantify geopolitical risks affecting agricultural supply chains.
    This might aggregate outputs from the other classes in this module.
    """

    def __init__(self):
        """
        Initializes the GeopoliticalRiskIndex.
        """
        self.risk_components = {
            "shipping_chokepoints": {"weight": 0.3, "current_score": 0}, # Score from ShippingChokepointVulnerability
            "conflict_zones": {"weight": 0.4, "current_score": 0},      # Score from ConflictZoneProduction
            "trade_policy": {"weight": 0.3, "current_score": 0}         # Score from TradePolicySanctionImpact
        }
        self.overall_risk_score = 0

    def calculate_component_score(self, component_name, scenario_outputs):
        """
        Calculates a normalized risk score for a specific component based on simulation outputs.
        This is a placeholder for a more detailed scoring methodology.

        Args:
            component_name (str): The name of the risk component (e.g., 'shipping_chokepoints').
            scenario_outputs (list of dicts): Outputs from the simulation methods of relevant classes.

        Returns:
            float: A normalized risk score (e.g., 0-10).
        """
        # Example simplified scoring:
        score = 0
        if not scenario_outputs:
            return 0

        if component_name == "shipping_chokepoints":
            # Count number of high-impact disruptions
            high_impact_count = sum(1 for s in scenario_outputs if s.get("estimated_impact_level") == "High")
            score = min(high_impact_count * 2.5, 10) # Max score of 10
        elif component_name == "conflict_zones":
            # Average severity score
            severities = [s.get("overall_severity_score", 0) for s in scenario_outputs if "overall_severity_score" in s]
            if severities:
                score = sum(severities) / len(severities) # Assuming severity score is 0-10
            else:
                score = 0
        elif component_name == "trade_policy":
            # Consider number and severity of active impactful restrictions
            high_impact_restrictions = 0
            for s_output_list in scenario_outputs: # scenario_outputs might be a list of lists of dicts here
                for s in s_output_list:
                    if isinstance(s, dict) and s.get("food_security_impact_level_in_dependent_nations") == "High":
                        high_impact_restrictions +=1
            score = min(high_impact_restrictions * 3, 10)


        self.risk_components[component_name]["current_score"] = score
        return score

    def calculate_overall_risk_index(self):
        """
        Calculates the overall geopolitical risk index based on weighted component scores.

        Returns:
            float: The overall geopolitical risk score.
        """
        self.overall_risk_score = 0
        for component, details in self.risk_components.items():
            self.overall_risk_score += details["weight"] * details["current_score"]
        return self.overall_risk_score

    def get_risk_assessment_summary(self):
        """
        Provides a summary of the current geopolitical risk assessment.

        Returns:
            dict: A summary including component scores and the overall index.
        """
        return {
            "overall_geopolitical_risk_index": self.overall_risk_score,
            "component_scores": self.risk_components,
            "assessment_timestamp": "YYYY-MM-DD HH:MM:SS" # Placeholder for actual timestamp
        }


class SupplyChainDiversificationModel:
    """
    Evaluates strategies for diversifying supply chains to mitigate geopolitical risks.
    Placeholder for now.
    """

    def __init__(self, current_sourcing_map=None):
        """
        Initializes with current sourcing map.
        Args:
            current_sourcing_map (dict): {'commodity': {'source_country': 'percentage_share'}}
        """
        self.current_sourcing_map = current_sourcing_map if current_sourcing_map else {}
        self.alternative_sources_database = { # Example
            'wheat': ['Canada', 'Australia', 'Argentina', 'France', 'Kazakhstan'],
            'corn': ['Brazil', 'Argentina', 'South Africa'],
            'palm_oil': ['Malaysia', 'Thailand', 'Colombia']
        }

    def identify_concentration_risks(self, commodity, threshold_percent=30):
        """
        Identifies commodities with high sourcing concentration from few countries.
        """
        risks = []
        if commodity in self.current_sourcing_map:
            for source, share in self.current_sourcing_map[commodity].items():
                if share >= threshold_percent:
                    risks.append({
                        'commodity': commodity,
                        'source_country': source,
                        'concentration_percent': share,
                        'risk_level': 'High' if share >= 50 else 'Medium'
                    })
        return risks

    def evaluate_alternative_sources(self, commodity, current_source_to_replace=None):
        """
        Evaluates potential alternative sources for a given commodity.
        Considers factors like production capacity, cost, logistics, political stability (simplified).
        """
        alternatives = []
        if commodity in self.alternative_sources_database:
            for alt_source in self.alternative_sources_database[commodity]:
                if alt_source == current_source_to_replace:
                    continue
                alternatives.append({
                    'source': alt_source,
                    'estimated_capacity_available_mt': "Placeholder", # Would require data
                    'estimated_landed_cost_increase_percent': "Placeholder", # Relative to current
                    'logistics_complexity': "low/medium/high", # Placeholder
                    'geopolitical_stability_rating': "Placeholder (1-5)" # Placeholder
                })
        return alternatives

    def recommend_diversification_actions(self, commodity, risk_level_threshold='Medium'):
        """
        Recommends actions based on concentration risks and alternative source viability.
        """
        recommendations = []
        concentration_risks = self.identify_concentration_risks(commodity)
        for risk in concentration_risks:
            if (risk_level_threshold == 'Medium' and risk['risk_level'] in ['Medium', 'High']) or \
               (risk_level_threshold == 'High' and risk['risk_level'] == 'High'):
                alternatives = self.evaluate_alternative_sources(commodity, risk['source_country'])
                recommendations.append({
                    'identified_risk': risk,
                    'action': f"Develop alternative sourcing from: {[alt['source'] for alt in alternatives]}",
                    'potential_alternatives': alternatives
                })
        if not recommendations and commodity in self.current_sourcing_map:
             recommendations.append({'commodity': commodity, 'action': 'Current sourcing appears diversified or below risk threshold.'})
        elif commodity not in self.current_sourcing_map:
            recommendations.append({'commodity': commodity, 'action': 'No sourcing map data for this commodity.'})

        return recommendations 

class GeopoliticalDisruptionSupplyChain:
    """
    Main class to simulate and analyze the impacts of geopolitical disruptions on agricultural supply chains.
    This class orchestrates various sub-models for different types of geopolitical events.
    """

    def __init__(self, initial_data=None):
        """
        Initializes the GeopoliticalDisruptionSupplyChain simulator.

        Args:
            initial_data (dict, optional): Initial data for commodity flows, prices, key regions, etc.
                                           Example: {'global_wheat_trade_volume_mt': 200, 
                                                     'key_importers': {'Egypt': {'wheat_demand_mt': 12}}}
        """
        self.initial_data = initial_data if initial_data else {}
        self.shipping_chokepoint_model = ShippingChokepointVulnerability()
        self.conflict_zone_model = ConflictZoneProduction()
        self.trade_policy_model = TradePolicySanctionImpact()
        self.risk_index_model = GeopoliticalRiskIndex()
        self.diversification_model = SupplyChainDiversificationModel( # Example current sourcing map
            current_sourcing_map={
                'wheat': {'Russia': 30, 'Ukraine': 15, 'Canada': 20, 'USA': 15, 'Australia': 10, 'Other': 10},
                'corn': {'USA': 40, 'Brazil': 25, 'Argentina': 15, 'Ukraine': 10, 'Other': 10}
            }
        )
        self.simulation_results = []

    def run_chokepoint_disruption_scenario(self, chokepoint_name, disruption_type, duration_weeks, affected_commodities):
        """
        Runs a simulation for a specific chokepoint disruption.
        """
        impact = self.shipping_chokepoint_model.model_vulnerability(
            chokepoint_name=chokepoint_name,
            disruption_scenario=disruption_type,
            duration_days=duration_weeks * 7,
            affected_commodities=affected_commodities
        )
        result = {
            "scenario_type": "Shipping Chokepoint Disruption",
            "details": impact
        }
        self.simulation_results.append(result)
        return result

    def run_conflict_impact_scenario(self, region_name, conflict_intensity, duration_months, affected_commodities):
        """
        Runs a simulation for a conflict in a key agricultural zone.
        """
        impact = self.conflict_zone_model.simulate_production_impact(
            region=region_name,
            conflict_intensity=conflict_intensity,
            duration_months=duration_months,
            affected_crops=affected_commodities
        )
        result = {
            "scenario_type": "Conflict Zone Impact",
            "details": impact
        }
        self.simulation_results.append(result)
        return result

    def run_trade_policy_scenario(self, commodity, restricting_country, policy_type, restriction_level_percent=None, duration_months=None):
        """
        Runs a simulation for a new trade policy or sanction.
        """
        impact = self.trade_policy_model.simulate_export_restriction_impact(
            commodity=commodity,
            restricting_country=restricting_country,
            policy_type=policy_type,
            restriction_level_percent=restriction_level_percent,
            duration_months=duration_months
        )
        market_responses = self.trade_policy_model.assess_market_response_strategies(impact)
        result = {
            "scenario_type": "Trade Policy/Sanction Impact",
            "details": impact,
            "market_responses": market_responses
        }
        self.simulation_results.append(result)
        return result

    def update_geopolitical_risk_index(self):
        """
        Updates the overall geopolitical risk index based on current simulation results or other inputs.
        """
        chokepoint_outputs = [res['details'] for res in self.simulation_results if res['scenario_type'] == "Shipping Chokepoint Disruption" and 'details' in res]
        conflict_outputs = [res['details'] for res in self.simulation_results if res['scenario_type'] == "Conflict Zone Impact" and 'details' in res]
        trade_policy_outputs_details = [res['details'] for res in self.simulation_results if res['scenario_type'] == "Trade Policy/Sanction Impact" and 'details' in res]

        self.risk_index_model.calculate_component_score("shipping_chokepoints", chokepoint_outputs)
        self.risk_index_model.calculate_component_score("conflict_zones", conflict_outputs)
        # The TradePolicySanctionImpact.calculate_component_score expects a list of dicts.
        # Each 'details' from a trade_policy_scenario is a dict. So, trade_policy_outputs_details is already a list of dicts.
        # However, the scoring logic in GeopoliticalRiskIndex.calculate_component_score for 'trade_policy' iterates over a list of lists.
        # To match this, we wrap trade_policy_outputs_details in another list if it's not empty.
        # Or, better, adjust the GeopoliticalRiskIndex.calculate_component_score for 'trade_policy' to expect a flat list of dicts.
        # For now, adjusting the call here:
        self.risk_index_model.calculate_component_score("trade_policy", [trade_policy_outputs_details] if trade_policy_outputs_details else [])


        overall_index = self.risk_index_model.calculate_overall_risk_index()
        summary = self.risk_index_model.get_risk_assessment_summary()
        summary['overall_calculated_index'] = overall_index
        
        # Ensure datetime is imported if used here directly, or handled inside the class if preferred.
        # For this structure, importing here is fine.
        try:
            from datetime import datetime
            summary['assessment_timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        except ImportError:
            summary['assessment_timestamp'] = "Timestamp unavailable"


        risk_result = {"scenario_type": "Geopolitical Risk Index Update", "details": summary}
        self.simulation_results.append(risk_result)
        return risk_result

    def analyze_supply_chain_diversification(self, commodity, risk_threshold='Medium'):
        """
        Analyzes and recommends supply chain diversification strategies.
        """
        recommendations = self.diversification_model.recommend_diversification_actions(commodity, risk_threshold)
        result = {
            "scenario_type": "Supply Chain Diversification Analysis",
            "commodity": commodity,
            "risk_threshold_applied": risk_threshold,
            "recommendations": recommendations
        }
        self.simulation_results.append(result)
        return result

    def get_all_simulation_results(self):
        """
        Returns all accumulated simulation results.
        """
        return self.simulation_results

    def clear_simulation_results(self):
        """
        Clears all stored simulation results.
        """
        self.simulation_results = []
        return {"status": "Simulation results cleared"}

if __name__ == '__main__':
    # This import is needed for the example usage if GeopoliticalDisruptionSupplyChain itself
    # relies on datetime internally and it's not imported at the top of the file.
    # However, the current structure has datetime import inside update_geopolitical_risk_index.
    # from datetime import datetime 

    simulator = GeopoliticalDisruptionSupplyChain(
        initial_data={'global_wheat_trade_volume_mt': 200, 'key_importers': {'Egypt': {'wheat_demand_mt': 12}}}
    )

    # Run a chokepoint scenario
    choke_result = simulator.run_chokepoint_disruption_scenario(
        chokepoint_name="Suez Canal",
        disruption_type="Blockage",
        duration_weeks=2,
        affected_commodities=["grains", "oilseeds"]
    )
    print("Chokepoint Disruption Result:", choke_result)

    # Run a conflict scenario
    conflict_result = simulator.run_conflict_impact_scenario(
        region_name="Ukraine/Black Sea Region",
        conflict_intensity="High",
        duration_months=6,
        affected_commodities=["wheat", "corn", "sunflower oil"]
    )
    print("\nConflict Impact Result:", conflict_result)

    # Run a trade policy scenario
    trade_policy_result = simulator.run_trade_policy_scenario(
        commodity="wheat",
        restricting_country="Major Exporter X",
        policy_type="export_ban",
        duration_months=3
    )
    print("\nTrade Policy Result:", trade_policy_result)

    # Update and get risk index
    # Ensure the risk index calculation for trade_policy uses the output correctly
    risk_index_result = simulator.update_geopolitical_risk_index()
    print("\nGeopolitical Risk Index:", risk_index_result)

    # Analyze diversification for wheat
    diversification_result = simulator.analyze_supply_chain_diversification(commodity='wheat', risk_threshold='Medium')
    print("\nWheat Diversification Analysis:", diversification_result)

    # Analyze diversification for corn
    diversification_corn_result = simulator.analyze_supply_chain_diversification(commodity='corn')
    print("\nCorn Diversification Analysis:", diversification_corn_result)

    # Get all results
    # all_results = simulator.get_all_simulation_results()
    # print("\nAll Simulation Results:", all_results)

    # Clear results
    # clear_status = simulator.clear_simulation_results()
    # print("\nClear Status:", clear_status)