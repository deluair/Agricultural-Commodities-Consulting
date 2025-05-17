# This module will handle simulations related to Trade Flow Reconfiguration & Market Access.

class BilateralRelationshipEvolution:
    """
    Models the evolution of bilateral trade relationships and their impact on agricultural commodity flows.
    """
    def __init__(self):
        self.trade_relationships = {
            "US-China": {
                "current_status": "Phase One Deal in place, but tensions remain. Significant agricultural trade, especially soybeans, sorghum, pork.",
                "key_commodities": ["soybeans", "corn", "pork", "sorghum", "cotton"],
                "positive_scenarios": ["tariff reduction", "increased import quotas", "resolution of SPS issues"],
                "negative_scenarios": ["new tariffs", "retaliatory measures", "geopolitical flare-ups impacting trade"],
                "historical_trade_usd_billion": {"2018": 20.0, "2019": 10.0, "2020": 30.0, "2021": 35.0, "2022": 38.0},
                "impact_potential": "high" # Can significantly shift global trade flows
            },
            "EU-Russia": {
                "current_status": "Significant disruption due to sanctions following Ukraine invasion. Historically, EU exported processed foods, Russia exported grains.",
                "key_commodities": ["grains (wheat, barley)", "fertilizers", "processed foods"],
                "positive_scenarios": ["easing of sanctions (unlikely in short term)", "new trade routes bypassing conflict zones (limited)"],
                "negative_scenarios": ["prolonged conflict", "further sanctions", "weaponization of food/fertilizer exports"],
                "historical_trade_usd_billion": {"pre_2022_agri_food_turnover_approx": 30.0}, # Combined agri-food
                "impact_potential": "medium_high" # Affects regional food security, global fertilizer prices
            },
            "India-MiddleEast": {
                "current_status": "Growing corridor, focus on food security for ME, market access for India. UAE is a key hub.",
                "key_commodities": ["rice (basmati)", "wheat", "sugar", "fruits & vegetables", "meat"],
                "positive_scenarios": ["comprehensive economic partnership agreements (CEPAs)", "investment in supply chains", "harmonization of standards"],
                "negative_scenarios": ["SPS barriers", "geopolitical instability in ME", "competition from other suppliers"],
                "trade_growth_potential_percent_annual": 5.0, # Illustrative
                "impact_potential": "medium"
            },
            "Africa-Europe": {
                "current_status": "Long-standing trade, often involves Economic Partnership Agreements (EPAs). Focus on raw commodities from Africa, processed from EU.",
                "key_commodities": ["cocoa", "coffee", "fruits", "vegetables", "fish", # Africa to EU
                                  "wheat", "dairy", "processed foods" # EU to Africa
                                 ],
                "positive_scenarios": ["increased African Continental Free Trade Area (AfCFTA) coherence boosting intra-African trade then EU trade", "investment in African agri-processing", "sustainable sourcing initiatives"],
                "negative_scenarios": ["EU SPS/TBT measures perceived as barriers", "debt sustainability issues in African nations", "climate change impacts on African production"],
                "impact_potential": "medium"
            },
            "LatinAmerica-Asia": {
                "current_status": "Rapidly expanding, driven by Asian demand for protein, grains, fruits. China is a major buyer.",
                "key_commodities": ["soybeans", "beef", "poultry", "fruits (cherries, avocados, citrus)", "coffee"],
                "positive_scenarios": ["new trade agreements (e.g. CPTPP expansion)", "infrastructure development (ports, logistics)", "diversification of Asian importers"],
                "negative_scenarios": ["increased protectionism in Asia", "over-reliance on single markets (e.g. China)", "environmental concerns (deforestation) leading to boycotts"],
                "historical_trade_growth_rate_percent_pa_approx": 7.0, # Illustrative for key commodities
                "impact_potential": "high"
            }
        }

    def get_relationship_details(self, country_pair_key: str):
        """
        Retrieves details for a specific trade relationship.
        Example: country_pair_key = "US-China"
        """
        return self.trade_relationships.get(country_pair_key, "Relationship not found.")

    def model_impact(self, country_pair_key: str, scenario_type: str, specific_event: str, magnitude_factor: float = 1.0):
        """
        Model bilateral relationship evolution impact.
        - country_pair_key: Key from self.trade_relationships (e.g., "US-China")
        - scenario_type: 'positive' or 'negative'
        - specific_event: Description of the event (e.g., "new tariffs on soybeans")
        - magnitude_factor: A multiplier for the typical impact (e.g., 0.5 for minor, 2.0 for major event)

        Returns a dictionary describing the potential impact.
        """
        if country_pair_key not in self.trade_relationships:
            return {"error": f"Trade relationship {country_pair_key} not found."}

        relationship = self.trade_relationships[country_pair_key]
        impact_description = f"Simulating {scenario_type} scenario for {country_pair_key} due to '{specific_event}' with magnitude {magnitude_factor}."
        potential_impacts = []

        # Generic impact logic, can be expanded
        base_impact_score = 10 * magnitude_factor # Arbitrary base score

        if scenario_type == "positive":
            change_direction = "increase"
            effect_on_commodities = f"Potential {change_direction} in trade for {', '.join(relationship['key_commodities'])}."
            if "tariff reduction" in specific_event.lower():
                potential_impacts.append(f"Lower prices for consumers in importing country, higher volumes.")
                base_impact_score *= 1.2
            elif "increased import quotas" in specific_event.lower():
                potential_impacts.append(f"Increased market access for exporting country.")
                base_impact_score *= 1.1
        elif scenario_type == "negative":
            change_direction = "decrease"
            effect_on_commodities = f"Potential {change_direction} in trade for {', '.join(relationship['key_commodities'])}."
            if "tariffs" in specific_event.lower() or "sanction" in specific_event.lower():
                potential_impacts.append(f"Higher prices for consumers, trade diversion, potential supply shortages.")
                base_impact_score *= 1.5
            elif "geopolitical flare-ups" in specific_event.lower():
                 potential_impacts.append(f"Supply chain disruptions, increased risk premium, reduced investment.")
                 base_impact_score *= 1.3
        else:
            return {"error": "Invalid scenario_type. Must be 'positive' or 'negative'."}

        potential_impacts.append(effect_on_commodities)
        final_impact_score = base_impact_score * (2 if relationship['impact_potential'] == 'high' else (1.5 if relationship['impact_potential'] == 'medium_high' else 1))

        return {
            "relationship": country_pair_key,
            "event": specific_event,
            "scenario_type": scenario_type,
            "description": impact_description,
            "potential_impacts_summary": potential_impacts,
            "affected_commodities": relationship['key_commodities'],
            "estimated_impact_score": round(final_impact_score, 2) # Higher score = more significant impact
        }

class BarrierDevelopment:
    """
    Simulates the development of new trade barriers or the intensification of existing ones.
    """
    def __init__(self):
        self.barrier_types = {
            "tariff": {"max_increase_percent": 50, "typical_scope": "specific_commodities_countries"},
            "quota": {"max_reduction_percent": 75, "typical_scope": "sensitive_commodities"},
            "sps_measure": {"complexity_increase_factor": 2, "typical_scope": "response_to_pest_disease_event"},
            "tbt_measure": {"stringency_increase_factor": 1.5, "typical_scope": "consumer_safety_environmental_concerns"},
            "export_restriction": {"duration_months": [3, 6, 12], "typical_scope": "domestic_food_security"}
        }
        self.potential_triggers = [
            "domestic_industry_pressure", "retaliation_to_other_country_action",
            "food_safety_scare", "environmental_concern_escalation", "national_security_concerns"
        ]
        self.commodity_vulnerability = { # Example: arbitrary vulnerability scores
            "wheat": {"tariff": 0.6, "quota": 0.5, "sps": 0.7, "export_restriction": 0.8},
            "beef": {"tariff": 0.7, "quota": 0.8, "sps": 0.9, "tbt": 0.5},
            "fruits_vegetables": {"tariff": 0.5, "quota": 0.4, "sps": 0.8, "tbt": 0.7}
        }

    def simulate_new_barrier(self, region: str, commodity: str, barrier_type_key: str, trigger_event: str):
        """
        Simulates the impact of a new trade barrier.
        """
        if barrier_type_key not in self.barrier_types:
            return {"error": f"Unknown barrier type: {barrier_type_key}"}
        if commodity not in self.commodity_vulnerability:
            return {"error": f"Commodity {commodity} not in vulnerability database."}

        barrier_spec = self.barrier_types[barrier_type_key]
        vulnerability = self.commodity_vulnerability[commodity].get(barrier_type_key, 0.5) # Default vulnerability

        impact_description = f"New '{barrier_type_key}' imposed on '{commodity}' in '{region}' due to '{trigger_event}'."
        potential_impact = {}

        if barrier_type_key == "tariff":
            increase = barrier_spec["max_increase_percent"] * vulnerability
            potential_impact = {"tariff_increase_percent": increase, "estimated_trade_reduction_percent": increase * 0.5} # Simplified
        elif barrier_type_key == "quota":
            reduction = barrier_spec["max_reduction_percent"] * vulnerability
            potential_impact = {"quota_reduction_percent": reduction, "estimated_market_share_loss_percent": reduction * 0.6}
        elif barrier_type_key == "sps_measure":
            complexity_increase = barrier_spec["complexity_increase_factor"] * vulnerability
            potential_impact = {"sps_complexity_factor": complexity_increase, "estimated_compliance_cost_increase_percent": complexity_increase * 10}
        elif barrier_type_key == "tbt_measure":
            stringency_increase = barrier_spec["stringency_increase_factor"] * vulnerability
            potential_impact = {"tbt_stringency_factor": stringency_increase, "estimated_market_access_difficulty_increase": stringency_increase * 0.3}
        elif barrier_type_key == "export_restriction":
            duration_idx = min(int(vulnerability * len(barrier_spec["duration_months"])), len(barrier_spec["duration_months"]) - 1)
            duration = barrier_spec["duration_months"][duration_idx]
            potential_impact = {"restriction_duration_months": duration, "estimated_global_price_spike_percent": vulnerability * 20}

        return {
            "scenario": impact_description,
            "trigger": trigger_event,
            "barrier_details": barrier_spec,
            "vulnerability_score_used": vulnerability,
            "potential_impact": potential_impact
        }

    def assess_escalation_risk(self, initial_barrier: dict, retaliation_probability: float = 0.3):
        """
        Assesses the risk of retaliatory barriers or escalation.
        """
        if initial_barrier.get("potential_impact"):
            # Simplified: higher impact -> higher retaliation risk
            severity_factor = sum(initial_barrier["potential_impact"].values()) / 100 # Rough measure
            escalation_risk_score = severity_factor * retaliation_probability
            return {
                "initial_barrier_summary": initial_barrier.get("scenario"),
                "retaliation_probability": retaliation_probability,
                "estimated_escalation_risk_score": min(escalation_risk_score, 1.0), # Cap at 1.0
                "possible_retaliation_measures": ["counter-tariffs", "alternative_sps_claims", "import_slowdowns"]
            }
        return {"error": "Invalid initial barrier data for escalation assessment."}

class TradeAgreementImpact:
    """
    Analyzes the impact of major multilateral and bilateral trade agreements.
    """
    def __init__(self):
        self.agreements = {
            "CPTPP": { # Comprehensive and Progressive Agreement for Trans-Pacific Partnership
                "members": ["Australia", "Brunei", "Canada", "Chile", "Japan", "Malaysia", "Mexico", "New Zealand", "Peru", "Singapore", "Vietnam", "UK"], # UK accession pending full ratification
                "key_agri_provisions": "Tariff elimination/reduction for many agricultural products, SPS chapter, rules of origin.",
                "potential_impact_agri": "Increased trade for members, particularly for dairy, meat, grains, horticulture. Potential trade diversion from non-members. Enhanced regulatory coherence.",
                "example_commodities_benefiting": ["beef (Australia to Japan)", "dairy (NZ to Canada)", "pork (Canada to Vietnam)"]
            },
            "RCEP": { # Regional Comprehensive Economic Partnership
                "members": ["ASEAN (10 nations)", "China", "Japan", "South Korea", "Australia", "New Zealand"],
                "key_agri_provisions": "Modest tariff reductions for some agri products (sensitive sectors often excluded or have long phase-ins), SPS and TBT measures, customs procedures.",
                "potential_impact_agri": "Gradual increase in intra-RCEP trade, supply chain integration. Impact varies significantly by commodity and country pair due to existing FTAs.",
                "example_commodities_benefiting": ["processed foods (within ASEAN)", "some seafood (Japan to China)"]
            },
            "AfCFTA": { # African Continental Free Trade Area
                "members": "Most African Union member states (operational phase ongoing)",
                "key_agri_provisions": "Aim to eliminate tariffs on 90% of goods, address non-tariff barriers. Rules of origin and SPS harmonization are critical ongoing work.",
                "potential_impact_agri": "Significant potential to boost intra-African agricultural trade, improve food security, stimulate agribusiness investment. Challenges in implementation and infrastructure.",
                "example_commodities_benefiting": ["grains (regional surplus to deficit areas)", "horticulture", "livestock products"]
            },
            "EU_Bilateral_FTAs": {
                "examples": ["EU-Canada (CETA)", "EU-Japan (EPA)", "EU-Mercosur (pending ratification)", "EU-Vietnam (EVFTA)"],
                "key_agri_provisions": "Varies by agreement. Often tariff reductions/eliminations (TRQs for sensitive products like beef, dairy, sugar), GI protection, SPS cooperation.",
                "potential_impact_agri": "Significant market access improvements for specific commodities, increased competition. GIs are a key EU offensive interest.",
                "example_commodities_benefiting": ["cheese (EU to Canada/Japan)", "wine (EU to various)", "beef (Mercosur to EU, if ratified)"]
            },
            "USMCA": { # United States-Mexico-Canada Agreement
                "members": ["USA", "Canada", "Mexico"],
                "key_agri_provisions": "Maintained largely tariff-free agricultural trade from NAFTA. Specific provisions for dairy (Canada increased US access), poultry (US to Canada), wheat grading (US-Canada). Biotechnology chapter.",
                "potential_impact_agri": "Provides stability and predictability for North American agri trade. Resolved some irritants, but some sector-specific tensions remain.",
                "example_commodities_benefiting": ["US dairy to Canada", "corn/soybeans (US to Mexico)"]
            }
        }

    def get_agreement_details(self, agreement_name: str):
        """
        Retrieves details for a specific trade agreement.
        """
        return self.agreements.get(agreement_name, {"error": f"Agreement {agreement_name} not found."})

    def analyze_impact_on_commodity_flow(self, agreement_name: str, commodity: str, exporting_country: str, importing_country: str):
        """
        Analyzes the potential impact of an agreement on a specific commodity flow.
        This is a simplified qualitative analysis.
        """
        agreement = self.agreements.get(agreement_name)
        if not agreement:
            return {"error": f"Agreement {agreement_name} not found."}

        impact_statement = f"Analysis for {commodity} from {exporting_country} to {importing_country} under {agreement_name}: "
        
        exporter_is_member = False
        importer_is_member = False
        
        asean_countries = ["Indonesia", "Thailand", "Vietnam", "Malaysia", "Philippines", "Singapore", "Brunei", "Cambodia", "Laos", "Myanmar"]
        # Temp list for current agreement's members, resolving groups like ASEAN
        resolved_members = []
        if isinstance(agreement["members"], list):
            for member_entry in agreement["members"]:
                if isinstance(member_entry, str) and member_entry.startswith("ASEAN"):
                    resolved_members.extend(asean_countries)
                elif isinstance(member_entry, str):
                    resolved_members.append(member_entry)
        elif isinstance(agreement["members"], str): # e.g. "Most African Union member states"
            if agreement["members"].startswith("ASEAN"): # Should not happen if data is consistent, but defensive
                resolved_members.extend(asean_countries)
            # For broad string descriptors like AfCFTA, direct check is hard. Logic below handles it.
            pass 

        if exporting_country in resolved_members:
            exporter_is_member = True
        if importing_country in resolved_members:
            importer_is_member = True

        # Special handling for AfCFTA due to broad member string
        if agreement_name == "AfCFTA" and agreement["members"] == "Most African Union member states":
            # This is a placeholder for a real check against a list of AU/AfCFTA members
            # For demo, assume it's plausible if countries sound African (very simplified)
            african_example_countries = ["Nigeria", "South Africa", "Kenya", "Egypt", "Ghana", "Ethiopia", "Algeria", "Morocco", "Angola", "Tanzania", "Ivory Coast"]
            if exporting_country in african_example_countries : exporter_is_member = True # Simplified check
            if importing_country in african_example_countries : importer_is_member = True # Simplified check

        if not (exporter_is_member and importer_is_member):
            impact_statement += "No direct impact as one or both countries are not definitively members of the agreement based on available data. Potential for trade diversion."
            return {"analysis": impact_statement, "trade_change_potential": "Low/Indirect"}

        impact_statement += f"Positive. {agreement_name} generally aims to {agreement['key_agri_provisions'].lower().split(',')[0]}. "
        trade_change_potential = "Medium" 

        if "example_commodities_benefiting" in agreement:
            for ex_commodity_flow in agreement["example_commodities_benefiting"]:
                if commodity in ex_commodity_flow and (exporting_country in ex_commodity_flow or importing_country in ex_commodity_flow):
                    impact_statement += f" This commodity is often cited as benefiting: {ex_commodity_flow}."
                    if (agreement_name == "CPTPP" and commodity == "beef" and exporting_country == "Australia" and importing_country == "Japan") or \
                       (agreement_name == "USMCA" and commodity == "dairy" and exporting_country == "US" and importing_country == "Canada") or \
                       (agreement_name == "CPTPP" and commodity == "dairy" and exporting_country == "New Zealand" and importing_country == "Canada") or \
                       (agreement_name == "EU_Bilateral_FTAs" and commodity == "cheese" and exporting_country == "EU") : # Added common example
                        trade_change_potential = "High"
                    elif trade_change_potential == "Medium":
                        trade_change_potential = "Medium to High"
                    break 
        
        # Override for specific known high-impact scenarios not caught by generic examples
        if (agreement_name == "CPTPP" and commodity == "beef" and exporting_country == "Australia" and importing_country == "Japan") or \
           (agreement_name == "USMCA" and commodity == "dairy" and exporting_country == "US" and importing_country == "Canada") or \
           (agreement_name == "CPTPP" and commodity == "dairy" and exporting_country == "New Zealand" and importing_country == "Canada") or \
           (agreement_name == "EU_Bilateral_FTAs" and commodity == "cheese" and exporting_country == "EU" and (importing_country == "Canada" or importing_country == "Japan")):
            trade_change_potential = "High"
        elif agreement_name == "AfCFTA" and exporter_is_member and importer_is_member : 
             impact_statement += f"AfCFTA aims to boost intra-African trade by reducing tariffs and NTBs for {commodity}."
             trade_change_potential = "Medium (potential, implementation dependent)"
        
        return {"analysis": impact_statement, "trade_change_potential": trade_change_potential}

    def compare_agreement_impacts(self, commodity: str, exporting_country: str, importing_country: str, agreements_to_compare: list[str]):
        """
        Compares the potential impacts of multiple agreements on a specific trade flow.
        """
        comparison_results = {}
        for agreement_name in agreements_to_compare:
            comparison_results[agreement_name] = self.analyze_impact_on_commodity_flow(
                agreement_name, commodity, exporting_country, importing_country
            )
        return comparison_results

class InfrastructureLogisticsAdaptation:
    def assess_impact(self, infrastructure_type: str, region: str):
        """
        Assess infrastructure and logistics adaptation impact.
        - Port capacity expansion effect on export throughput
        - Inland logistics bottleneck cost implications
        - Cold chain infrastructure development for perishables
        - Rail vs. road vs. barge cost-benefit evolution
        - Geopolitical risk impact on shipping route viability
        """
        pass

class StandardEvolution:
    def project_evolution(self, standard_type: str):
        """
        Project food safety and sustainability standard evolution.
        - Maximum residue level restriction tightening trajectory
        - Traceability requirement implementation timeline
        - Carbon footprint documentation demand emergence
        - Deforestation-free requirement proliferation
        - Animal welfare standard adoption patterns
        """
        pass

class ConsumerPreferenceImpact:
    def simulate_impact(self, preference_type: str, market_segment: str):
        """
        Simulate consumer preference impact on trade patterns.
        - Organic demand growth by market
        - GMO acceptance evolution by region
        - Local sourcing preference strength by segment
        - Sustainability certification premium persistence
        - Novel protein substitution effect on traditional crop demand
        """
        pass

class MarketAccessAnalysis:
    """
    Analyzes market access conditions, including tariffs, quotas, and non-tariff barriers.
    """
    def __init__(self):
        self.tariff_data = {
            "wheat": {"US": {"mfn_avg_tariff_percent": 5.0, "specific_tariff_usd_mt": 10}, "EU": {"mfn_avg_tariff_percent": 7.5, "trq_volume_mt": 100000, "in_quota_tariff_percent": 2.0, "out_quota_tariff_percent": 15.0}},
            "corn": {"China": {"mfn_avg_tariff_percent": 12.0, "trq_volume_mt": 7200000, "in_quota_tariff_percent": 1.0, "out_quota_tariff_percent": 65.0}},
            "soybeans": {"EU": {"mfn_avg_tariff_percent": 0.0}, "India": {"mfn_avg_tariff_percent": 30.0}}
        }
        self.sps_measures = { # Example SPS measures
            "EU": {"max_residue_limits": {"pesticide_x": 0.01, "pesticide_y": 0.05}, "disease_free_zones_required": ["foot_and_mouth_disease"]},
            "Japan": {"fumigation_requirements": {"apples": "methyl_bromide"}, "pathogen_testing": {"poultry": "avian_influenza_h5n1"}}
        }
        self.tbt_measures = { # Example TBT measures
            "US": {"labeling_requirements": ["country_of_origin", "gmo_content"], "packaging_requirements": ["recyclable_materials"]},
            "Canada": {"product_quality_standards": {"maple_syrup_grade_a": True}, "testing_certification_needs": ["organic_products"]}
        }
        self.rules_of_origin = { # Example
            "USMCA": {"wheat": " wholly obtained or sufficient transformation (e.g., 50% regional value content)"}
        }

    def get_tariff_impact(self, commodity: str, exporting_country: str, importing_country: str, fob_price_usd_mt: float, volume_mt: float):
        """
        Estimates the impact of tariffs on import costs.
        Handles MFN tariffs, specific tariffs, and TRQs (simplified).
        """
        country_tariffs = self.tariff_data.get(commodity, {}).get(importing_country)
        if not country_tariffs:
            return {"message": f"No specific tariff data for {commodity} into {importing_country}. Assuming 0% tariff.", "tariff_cost_usd": 0, "effective_tariff_rate_percent": 0}

        total_value_fob = fob_price_usd_mt * volume_mt
        tariff_cost_usd = 0
        effective_rate = 0

        if "trq_volume_mt" in country_tariffs: # Tariff Rate Quota
            in_quota_volume = min(volume_mt, country_tariffs["trq_volume_mt"])
            out_quota_volume = volume_mt - in_quota_volume

            tariff_cost_usd += (fob_price_usd_mt * in_quota_volume) * (country_tariffs["in_quota_tariff_percent"] / 100.0)
            if out_quota_volume > 0:
                tariff_cost_usd += (fob_price_usd_mt * out_quota_volume) * (country_tariffs["out_quota_tariff_percent"] / 100.0)
            if total_value_fob > 0:
                effective_rate = (tariff_cost_usd / total_value_fob) * 100
        elif "mfn_avg_tariff_percent" in country_tariffs: # Ad valorem tariff
            rate = country_tariffs["mfn_avg_tariff_percent"] / 100.0
            tariff_cost_usd = total_value_fob * rate
            effective_rate = country_tariffs["mfn_avg_tariff_percent"]
        
        if "specific_tariff_usd_mt" in country_tariffs: # Specific tariff
            tariff_cost_usd += country_tariffs["specific_tariff_usd_mt"] * volume_mt
            if total_value_fob > 0: # Recalculate effective rate if specific tariff is also applied
                 effective_rate = (tariff_cost_usd / total_value_fob) * 100


        return {
            "commodity": commodity, "importing_country": importing_country,
            "fob_price_usd_mt": fob_price_usd_mt, "volume_mt": volume_mt,
            "total_fob_value_usd": total_value_fob,
            "tariff_cost_usd": round(tariff_cost_usd, 2),
            "landed_cost_before_other_fees_usd": round(total_value_fob + tariff_cost_usd, 2),
            "effective_tariff_rate_percent": round(effective_rate, 2),
            "tariff_details": country_tariffs
        }

    def check_sps_compliance(self, commodity: str, exporting_country: str, importing_country: str, product_attributes: dict):
        """
        Checks basic SPS compliance based on example data.
        `product_attributes` could be e.g. {"pesticide_residues": {"pesticide_x": 0.005}, "disease_status": "free_of_fmd"}
        """
        compliance_status = {"overall_compliant": True, "issues": []}
        sps_reqs = self.sps_measures.get(importing_country, {})

        if "max_residue_limits" in sps_reqs:
            for pesticide, limit in sps_reqs["max_residue_limits"].items():
                if product_attributes.get("pesticide_residues", {}).get(pesticide, 0) > limit:
                    compliance_status["overall_compliant"] = False
                    compliance_status["issues"].append(f"Exceeds MRL for {pesticide}: detected {product_attributes['pesticide_residues'][pesticide]}, limit {limit}")
        
        if "disease_free_zones_required" in sps_reqs:
            for disease in sps_reqs["disease_free_zones_required"]:
                if product_attributes.get("disease_status") != f"free_of_{disease}": # simplified check
                    # A real check would involve origin certification.
                    compliance_status["overall_compliant"] = False
                    compliance_status["issues"].append(f"Requires proof of being free from {disease}. Current status: {product_attributes.get('disease_status')}")
        
        if not compliance_status["issues"]:
            compliance_status["message"] = "No apparent SPS issues based on available data."
        
        return compliance_status

    def check_tbt_compliance(self, commodity: str, importing_country: str, product_attributes: dict):
        """
        Checks basic TBT compliance.
        `product_attributes` could be e.g. {"labeling": ["country_of_origin_present"], "packaging": "recyclable"}
        """
        compliance_status = {"overall_compliant": True, "issues": []}
        tbt_reqs = self.tbt_measures.get(importing_country, {})

        if "labeling_requirements" in tbt_reqs:
            for req_label in tbt_reqs["labeling_requirements"]:
                if req_label not in product_attributes.get("labeling", []): # Simple check, assumes presence means compliance
                    compliance_status["overall_compliant"] = False
                    compliance_status["issues"].append(f"Missing TBT labeling: {req_label}")

        if not compliance_status["issues"]:
            compliance_status["message"] = "No apparent TBT issues based on available data."
        return compliance_status
        
    def check_rules_of_origin(self, commodity: str, trade_agreement_context: str, product_origin_details: dict):
        """
        Placeholder for rules of origin check.
        `trade_agreement_context` e.g. "USMCA"
        `product_origin_details` e.g. {"regional_value_content_percent": 60, "last_transformation_country": "Mexico"}
        """
        roo = self.rules_of_origin.get(trade_agreement_context)
        if not roo or commodity not in roo: # Simplified: only checking if commodity mentioned in RoO
            return {"compliant": "Unknown", "message": f"No specific RoO data for {commodity} under {trade_agreement_context}."}
        
        # This is highly simplified. Real RoO are complex.
        # Example: if "wholly obtained" or RVC met.
        if "wholly obtained" in roo[commodity] or \
           (product_origin_details.get("regional_value_content_percent",0) >= 50 and "regional value content" in roo[commodity]):
            return {"compliant": True, "message": f"Likely meets RoO for {commodity} under {trade_agreement_context}."}
        else:
            return {"compliant": False, "message": f"May not meet RoO for {commodity} under {trade_agreement_context}. Details: {roo[commodity]}"}


    def analyze_market_access(self, commodity: str, exporting_country: str, importing_country: str, fob_price_usd_mt: float, volume_mt: float, product_attributes: dict, trade_agreement_context: str = None, product_origin_details:dict = None):
        """
        Comprehensive market access analysis using sub-components.
        """
        tariff_impact = self.get_tariff_impact(commodity, exporting_country, importing_country, fob_price_usd_mt, volume_mt)
        sps_check = self.check_sps_compliance(commodity, exporting_country, importing_country, product_attributes)
        tbt_check = self.check_tbt_compliance(commodity, importing_country, product_attributes)
        
        roo_check = {"compliant": "N/A", "message": "No trade agreement context provided for RoO."}
        if trade_agreement_context and product_origin_details:
            roo_check = self.check_rules_of_origin(commodity, trade_agreement_context, product_origin_details)

        overall_assessment = "Good"
        if tariff_impact.get("effective_tariff_rate_percent", 0) > 20:
            overall_assessment = "Challenging due to high tariffs."
        if not sps_check["overall_compliant"] or not tbt_check["overall_compliant"]:
            overall_assessment = "Significant non-tariff barriers."
        if roo_check.get("compliant") == False:
             overall_assessment = "Potential Rules of Origin issue."

        landed_cost_val_total = tariff_impact.get("landed_cost_before_other_fees_usd")
        landed_cost_estimate_per_mt = 0
        if landed_cost_val_total is not None:
            if volume_mt > 0:
                landed_cost_estimate_per_mt = landed_cost_val_total / volume_mt
            # if volume_mt is 0 and landed_cost_val_total is not None (e.g. 0), estimate is 0 (already set)
        elif volume_mt > 0: # landed_cost_val_total is None, meaning tariffs were likely 0 or data missing
                            # In this case, landed cost before other fees = FOB value. Per MT cost = FOB price.
            landed_cost_estimate_per_mt = fob_price_usd_mt
        # if landed_cost_val_total is None and volume_mt is 0, estimate is 0 (already set)

        return {
            "summary": f"Market access for {commodity} from {exporting_country} to {importing_country}: {overall_assessment}",
            "tariff_analysis": tariff_impact,
            "sps_analysis": sps_check,
            "tbt_analysis": tbt_check,
            "roo_analysis": roo_check,
            "landed_cost_estimate_usd_mt": round(landed_cost_estimate_per_mt, 2)
        }

class TradeFlowVolatilityModel:
    """
    Models trade flow volatility based on various shock events.
    """
    def __init__(self, market_access_analyzer: MarketAccessAnalysis):
        self.market_access_analyzer = market_access_analyzer
        self.shock_elasticities = { # Example price elasticities of supply/demand (commodity: {country: elasticity_supply, elasticity_demand})
            "wheat": {"default_export": -0.5, "default_import": 0.4}, # Negative for export supply, positive for import demand
            "corn": {"default_export": -0.6, "default_import": 0.5},
            "soybeans": {"default_export": -0.7, "default_import": 0.6}
        }

    def calculate_baseline_flow(self, commodity: str, exporting_country: str, importing_country: str, base_volume_mt: float, base_price_usd_mt: float):
        """
        Calculates baseline trade flow value and gets market access cost.
        """
        access_analysis = self.market_access_analyzer.analyze_market_access(
            commodity, exporting_country, importing_country, base_price_usd_mt, base_volume_mt, {}
        )
        tariff_cost_total = access_analysis["tariff_analysis"]["tariff_cost_usd"]
        landed_cost_mt = access_analysis["landed_cost_estimate_usd_mt"]
        
        return {
            "commodity": commodity, "from": exporting_country, "to": importing_country,
            "baseline_volume_mt": base_volume_mt, "baseline_fob_price_usd_mt": base_price_usd_mt,
            "baseline_fob_value_usd": base_volume_mt * base_price_usd_mt,
            "baseline_tariff_cost_usd": tariff_cost_total,
            "baseline_landed_cost_usd_mt": landed_cost_mt,
            "baseline_landed_value_usd": landed_cost_mt * base_volume_mt if landed_cost_mt else 0,
            "market_access_details": access_analysis
        }

    def simulate_trade_shock_impact(self, commodity: str, exporting_country: str, importing_country: str, 
                                    base_volume_mt: float, base_price_usd_mt: float, shock_event: dict):
        """
        Simulates the impact of a shock event on trade flow volume and price.
        Shock event example: 
        {"type": "tariff_increase", "importing_country": "China", "commodity": "soybeans", "details": {"new_tariff_percent": 25}}
        {"type": "export_ban", "exporting_country": "Russia", "commodity": "wheat", "details": {"duration_months": 6}}
        {"type": "sps_issue", "importing_country": "EU", "commodity": "beef", "exporting_country": "Brazil", "details": {"compliance_failure": True}}
        """
        baseline = self.calculate_baseline_flow(commodity, exporting_country, importing_country, base_volume_mt, base_price_usd_mt)
        
        adjusted_volume_mt = base_volume_mt
        adjusted_price_usd_mt = base_price_usd_mt
        remarks = [f"Shock: {shock_event['type']}"]

        # Simplified impact logic
        # A real model would use more complex supply/demand curves and elasticities.
        
        price_elasticity_supply = self.shock_elasticities.get(commodity, {}).get("default_export", -0.5)
        price_elasticity_demand = self.shock_elasticities.get(commodity, {}).get("default_import", 0.4)

        if shock_event["type"] == "tariff_increase" and shock_event.get("importing_country") == importing_country and shock_event.get("commodity") == commodity:
            old_tariff_rate = baseline["market_access_details"]["tariff_analysis"].get("effective_tariff_rate_percent",0) / 100.0
            new_tariff_rate = shock_event["details"]["new_tariff_percent"] / 100.0
            price_change_due_to_tariff = (new_tariff_rate - old_tariff_rate) * base_price_usd_mt
            
            # Assuming tariff partly absorbed by exporter, partly passed to importer
            price_increase_for_importer = price_change_due_to_tariff * 0.7 # 70% passed on
            adjusted_price_usd_mt += price_increase_for_importer
            
            # Volume change due to price change for importer (demand elasticity)
            percentage_price_change = (adjusted_price_usd_mt - base_price_usd_mt) / base_price_usd_mt if base_price_usd_mt else 0
            percentage_volume_change = percentage_price_change * price_elasticity_demand 
            adjusted_volume_mt *= (1 + percentage_volume_change)
            remarks.append(f"Tariff on {commodity} to {importing_country} increased. Estimated volume change: {percentage_volume_change*100:.2f}%.")

        elif shock_event["type"] == "export_ban" and shock_event.get("exporting_country") == exporting_country and shock_event.get("commodity") == commodity:
            adjusted_volume_mt = 0 # Complete ban from this source
            # This would cause price spikes globally, harder to model for a single flow without global context
            adjusted_price_usd_mt *= 1.2 # Illustrative 20% price jump for other sources
            remarks.append(f"{exporting_country} bans export of {commodity}. Volume from this source to zero.")

        elif shock_event["type"] == "sps_issue" and shock_event.get("importing_country") == importing_country and shock_event.get("commodity") == commodity and shock_event.get("exporting_country") == exporting_country:
            # Assume SPS issue reduces trade significantly or halts it
            adjusted_volume_mt *= 0.1 # 90% reduction
            remarks.append(f"SPS issue for {commodity} from {exporting_country} to {importing_country}. Volume drastically reduced.")
        
        # Recalculate access with new price/volume if needed (e.g. for specific tariffs)
        new_access_analysis = self.market_access_analyzer.analyze_market_access(
            commodity, exporting_country, importing_country, adjusted_price_usd_mt, adjusted_volume_mt, {}
        )
        new_tariff_cost_total = new_access_analysis["tariff_analysis"]["tariff_cost_usd"]
        new_landed_cost_mt = new_access_analysis["landed_cost_estimate_usd_mt"]


        return {
            "baseline": baseline,
            "shock_event": shock_event,
            "remarks": remarks,
            "adjusted_fob_price_usd_mt": round(adjusted_price_usd_mt,2),
            "adjusted_volume_mt": round(adjusted_volume_mt,2),
            "adjusted_fob_value_usd": round(adjusted_price_usd_mt * adjusted_volume_mt, 2),
            "adjusted_tariff_cost_usd": round(new_tariff_cost_total,2),
            "adjusted_landed_cost_usd_mt": round(new_landed_cost_mt,2) if new_landed_cost_mt else 0,
            "adjusted_landed_value_usd": round(new_landed_cost_mt * adjusted_volume_mt, 2) if new_landed_cost_mt else 0,
            "volume_change_percent": round(((adjusted_volume_mt - base_volume_mt) / base_volume_mt if base_volume_mt else 0) * 100, 2),
            "value_change_percent": round(((adjusted_price_usd_mt * adjusted_volume_mt - base_price_usd_mt * base_volume_mt) / (base_price_usd_mt * base_volume_mt) if base_price_usd_mt * base_volume_mt else 0) * 100, 2)
        }


class TradeFlowReconfigurationMarketAccess:
    """
    Main class to simulate trade flow reconfigurations based on market access changes.
    Orchestrates other classes in this module.
    """
    def __init__(self):
        self.bilateral_evolution = BilateralRelationshipEvolution()
        self.barrier_developer = BarrierDevelopment()
        self.agreement_analyzer = TradeAgreementImpact()
        self.market_analyzer = MarketAccessAnalysis()
        # Infrastructure, Standards, Consumer Prefs are more for qualitative context or deeper dives
        self.infra_logistics = InfrastructureLogisticsAdaptation()
        self.standard_evolution = StandardEvolution()
        self.consumer_prefs = ConsumerPreferenceImpact()
        self.volatility_model = TradeFlowVolatilityModel(self.market_analyzer)


    def simulate_scenario(self, scenario_details: dict):
        """
        Simulates a complex scenario involving multiple factors.
        Example scenario_details:
        {
            "name": "US-China Trade War Escalation",
            "base_flow": {"commodity": "soybeans", "exporting_country": "US", "importing_country": "China", "volume_mt": 20000000, "price_usd_mt": 450},
            "events": [
                {"type": "bilateral_relation_deterioration", "country_pair_key": "US-China", "event_details": "New round of retaliatory tariffs", "magnitude": 1.5},
                {"type": "new_barrier", "region": "China", "commodity": "soybeans", "barrier_type_key": "tariff", "trigger_event": "retaliation"},
                {"type": "trade_shock", "shock_event": {"type": "tariff_increase", "importing_country": "China", "commodity": "soybeans", "details": {"new_tariff_percent": 25}}}
            ],
            "alternative_markets_check": [ # What happens if US tries to sell to EU instead?
                 {"commodity": "soybeans", "exporting_country": "US", "importing_country": "EU", "volume_mt": 5000000, "price_usd_mt": 460}
            ]
        }
        """
        results = {"scenario_name": scenario_details["name"], "event_impacts": [], "flow_analyses": []}

        # Analyze base flow
        bf = scenario_details["base_flow"]
        base_flow_analysis = self.volatility_model.calculate_baseline_flow(bf["commodity"], bf["exporting_country"], bf["importing_country"], bf["volume_mt"], bf["price_usd_mt"])
        results["flow_analyses"].append({"flow_description": "Baseline Flow", "analysis": base_flow_analysis})
        
        current_volume = bf["volume_mt"]
        current_price = bf["price_usd_mt"]

        for event in scenario_details.get("events", []):
            if event["type"] == "bilateral_relation_deterioration":
                impact = self.bilateral_evolution.model_impact(event["country_pair_key"], "negative", event["event_details"], event.get("magnitude", 1.0))
                results["event_impacts"].append({"event_type": event["type"], "details": impact})
            elif event["type"] == "new_barrier":
                impact = self.barrier_developer.simulate_new_barrier(event["region"], event["commodity"], event["barrier_type_key"], event["trigger_event"])
                results["event_impacts"].append({"event_type": event["type"], "details": impact})
                # If barrier is a tariff, and it's the main flow, it will be handled by trade_shock
                # This is for general barrier development logging.
            elif event["type"] == "trade_shock":
                # Apply shock to the current state of the primary flow
                shock_impact = self.volatility_model.simulate_trade_shock_impact(
                    bf["commodity"], bf["exporting_country"], bf["importing_country"], 
                    current_volume, current_price, event["shock_event"]
                )
                results["flow_analyses"].append({"flow_description": f"After Shock: {event['shock_event']['type']}", "analysis": shock_impact})
                current_volume = shock_impact["adjusted_volume_mt"] # Update for subsequent shocks if any
                current_price = shock_impact["adjusted_fob_price_usd_mt"]

            elif event["type"] == "trade_agreement_change": # e.g. new FTA or exit
                # This would be more qualitative or involve adjusting parameters in MarketAccessAnalysis
                agreement_impact = self.agreement_analyzer.get_agreement_details(event["agreement_name"])
                results["event_impacts"].append({"event_type": event["type"], "details": agreement_impact, "change": event["change_description"]})

        # Analyze alternative markets
        for alt_flow_data in scenario_details.get("alternative_markets_check", []):
            alt_flow_analysis = self.volatility_model.calculate_baseline_flow(
                alt_flow_data["commodity"], alt_flow_data["exporting_country"], alt_flow_data["importing_country"],
                alt_flow_data["volume_mt"], alt_flow_data["price_usd_mt"]
            )
            # Here you could also apply any relevant shocks to the alternative flow
            results["flow_analyses"].append({"flow_description": f"Alternative Market: {alt_flow_data['exporting_country']} to {alt_flow_data['importing_country']}", "analysis": alt_flow_analysis})

        return results

if __name__ == '__main__':
    # Initialize the main simulation class
    trade_flow_simulator = TradeFlowReconfigurationMarketAccess()

    # Example 1: Analyze Market Access for a specific flow
    print("--- Example 1: Market Access Analysis ---")
    market_access_result = trade_flow_simulator.market_analyzer.analyze_market_access(
        commodity="corn", 
        exporting_country="US", 
        importing_country="China", 
        fob_price_usd_mt=250, 
        volume_mt=1000000,
        product_attributes={"pesticide_residues": {"pesticide_x": 0.003}},
        trade_agreement_context="USMCA", # Not directly relevant for US-China but for RoO example
        product_origin_details= {"regional_value_content_percent": 70}
    )
    print(f"Market Access for Corn (US to China):")
    for key, value in market_access_result.items():
        if isinstance(value, dict):
            print(f"  {key}:")
            for sub_key, sub_value in value.items():
                 print(f"    {sub_key}: {sub_value}")
        else:
            print(f"  {key}: {value}")
    print("\n")

    # Example 2: Simulate impact of a new trade barrier
    print("--- Example 2: New Trade Barrier Simulation ---")
    barrier_sim_result = trade_flow_simulator.barrier_developer.simulate_new_barrier(
        region="EU", 
        commodity="beef", 
        barrier_type_key="sps_measure", 
        trigger_event="new animal disease concern in exporting region"
    )
    print(f"New SPS Measure on Beef to EU: {barrier_sim_result}\n")
    
    escalation_risk = trade_flow_simulator.barrier_developer.assess_escalation_risk(barrier_sim_result)
    print(f"Escalation risk for this barrier: {escalation_risk}\n")


    # Example 3: Analyze impact of a trade agreement
    print("--- Example 3: Trade Agreement Impact ---")
    agreement_analysis = trade_flow_simulator.agreement_analyzer.analyze_impact_on_commodity_flow(
        agreement_name="CPTPP", 
        commodity="dairy", 
        exporting_country="New Zealand", 
        importing_country="Canada"
    )
    print(f"CPTPP Impact on Dairy (NZ to Canada): {agreement_analysis}\n")
    
    agreement_comparison = trade_flow_simulator.agreement_analyzer.compare_agreement_impacts(
        commodity="wheat", exporting_country="Australia", importing_country="Indonesia", 
        agreements_to_compare=["CPTPP", "RCEP"]
    )
    print(f"Comparison for Wheat (Australia to Indonesia) under CPTPP vs RCEP: {agreement_comparison}\n")


    # Example 4: Bilateral Relationship Scenario
    print("--- Example 4: Bilateral Relationship Scenario ---")
    bilateral_impact = trade_flow_simulator.bilateral_evolution.model_impact(
        country_pair_key="US-China",
        scenario_type="negative",
        specific_event="Increased tensions over tech, spilling to agri tariffs",
        magnitude_factor=1.2
    )
    print(f"Impact of US-China Negative Scenario: {bilateral_impact}\n")

    # Example 5: Trade Flow Volatility due to a shock
    print("--- Example 5: Trade Flow Volatility ---")
    shock_details = {"type": "tariff_increase", "importing_country": "China", "commodity": "soybeans", "details": {"new_tariff_percent": 25}}
    volatility_result = trade_flow_simulator.volatility_model.simulate_trade_shock_impact(
        commodity="soybeans", 
        exporting_country="US", 
        importing_country="China", 
        base_volume_mt=20000000, 
        base_price_usd_mt=450,
        shock_event=shock_details
    )
    print(f"Volatility for Soybeans (US to China) after tariff shock:")
    for key, value in volatility_result.items():
        if isinstance(value, dict) and key != 'baseline' and key != 'market_access_details': # Avoid overly verbose prints for nested dicts
            print(f"  {key}: {{...}}") # Indicate a dictionary without printing all its content
        elif key == 'baseline' or key == 'market_access_details':
             print(f"  {key}:")
             for sub_key, sub_value in value.items():
                 print(f"    {sub_key}: {sub_value}")
        else:
            print(f"  {key}: {value}")
    print("\n")


    # Example 6: More Complex Scenario Simulation
    print("--- Example 6: Complex Scenario Simulation ---")
    complex_scenario = {
        "name": "Geopolitical Shift & Climate Event Affecting Wheat Trade",
        "base_flow": {"commodity": "wheat", "exporting_country": "Australia", "importing_country": "Indonesia", "volume_mt": 5000000, "price_usd_mt": 300},
        "events": [
            {"type": "bilateral_relation_deterioration", "country_pair_key": "India-MiddleEast", "event_details": "Regional instability affecting shipping", "magnitude": 0.8},
            {"type": "new_barrier", "region": "Indonesia", "commodity": "wheat", "barrier_type_key": "sps_measure", "trigger_event": "pest concern"},
            {"type": "trade_shock", "shock_event": {"type": "sps_issue", "importing_country": "Indonesia", "commodity": "wheat", "exporting_country":"Australia", "details": {"compliance_failure": True}}},
            {"type": "trade_agreement_change", "agreement_name": "RCEP", "change_description": "Improved customs procedures fully implemented for RCEP members."}
        ],
        "alternative_markets_check": [
             {"commodity": "wheat", "exporting_country": "Canada", "importing_country": "Indonesia", "volume_mt": 1000000, "price_usd_mt": 320}
        ]
    }
    complex_scenario_results = trade_flow_simulator.simulate_scenario(complex_scenario)
    print(f"Results for Complex Scenario: '{complex_scenario_results['scenario_name']}'")
    print(f"  Number of event impacts logged: {len(complex_scenario_results.get('event_impacts', []))}")
    print(f"  Number of flow analyses logged: {len(complex_scenario_results.get('flow_analyses', []))}")
    print("  Key findings from the last flow analysis (Wheat from Australia to Indonesia after SPS shock):")
    
    relevant_flow_analysis = None
    flow_analyses_list = complex_scenario_results.get('flow_analyses', [])
    for analysis_item in reversed(flow_analyses_list):
        current_analysis = analysis_item.get('analysis', {})
        baseline_info = current_analysis.get('baseline', {})
        
        if analysis_item.get("flow_description", "").startswith("After Shock") and \
           baseline_info.get("commodity") == complex_scenario["base_flow"]["commodity"] and \
           baseline_info.get("from") == complex_scenario["base_flow"]["exporting_country"] and \
           baseline_info.get("to") == complex_scenario["base_flow"]["importing_country"]:
            relevant_flow_analysis = current_analysis
            break
    
    if relevant_flow_analysis:
        # Using .get() with defaults for all potentially missing keys
        adj_vol = relevant_flow_analysis.get('adjusted_volume_mt', 'N/A')
        vol_change = relevant_flow_analysis.get('volume_change_percent', 0)
        adj_val = relevant_flow_analysis.get('adjusted_fob_value_usd', 'N/A')
        val_change = relevant_flow_analysis.get('value_change_percent', 0)
        remarks_list = relevant_flow_analysis.get('remarks', ['N/A'])

        vol_change_str = f"{vol_change:.2f}%" if isinstance(vol_change, (int,float)) else str(vol_change)
        val_change_str = f"{val_change:.2f}%" if isinstance(val_change, (int,float)) else str(val_change)
        adj_val_str = f"${adj_val:,}" if isinstance(adj_val, (int,float)) else str(adj_val)


        print(f"    Adjusted Volume: {adj_vol} MT (Change: {vol_change_str})")
        print(f"    Adjusted FOB Value: {adj_val_str} (Change: {val_change_str})")
        print(f"    Remarks: {'; '.join(remarks_list)}")
    else:
        print("    Relevant shocked flow analysis not found for detailed printout.")

    print("  Analysis for alternative (Canada to Indonesia):")
    alt_flow = None
    for analysis_item in flow_analyses_list:
        if "Alternative Market" in analysis_item.get("flow_description", "") and \
           "Canada to Indonesia" in analysis_item.get("flow_description", ""):
            alt_flow = analysis_item.get('analysis', {})
            break
            
    if alt_flow:
        base_vol = alt_flow.get('baseline_volume_mt', 'N/A')
        landed_cost = alt_flow.get('baseline_landed_cost_usd_mt', 'N/A')
        market_details = alt_flow.get('market_access_details', {})
        summary = market_details.get('summary', 'N/A')

        print(f"    Baseline Volume: {base_vol} MT")
        if isinstance(landed_cost, (int, float)):
            print(f"    Baseline Landed Cost/MT: ${landed_cost:.2f}")
        else:
            print(f"    Baseline Landed Cost/MT: {landed_cost}")
        print(f"    Market Access Summary: {summary}")
    else:
        print("    Alternative flow analysis (Canada to Indonesia) not found.") 