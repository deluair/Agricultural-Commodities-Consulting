# This module will handle simulations related to Climate Shock Impact & Yield Volatility. 

class YieldShockPropagation:
    def simulate_dynamics(self, region: str, shock_severity: float):
        """
        Simulate yield shock propagation dynamics.
        - Regional production shortfall correlation with global price movement
        - Exporter restriction probability modeling by shock severity
        - Import bill impact quantification for deficit economies
        - Food security vulnerability assessment framework
        - Stockpile drawdown behavior by country income category
        """
        pass

class ClimateVolatilityModel:
    """
    Models climate volatility, including temperature and precipitation anomalies,
    and their correlation with agricultural yield impacts.
    """

    def __init__(self, baseline_climate_data=None):
        """
        Initializes the ClimateVolatilityModel.

        Args:
            baseline_climate_data (dict, optional): Baseline climate data for key regions.
                                                    Example: {'region_A': {'avg_temp': 20, 'avg_precip': 500}}
        """
        self.baseline_climate_data = baseline_climate_data if baseline_climate_data else {
            'North America Plains': {'avg_temp_c': 15, 'avg_precip_mm': 600, 'primary_crop': 'wheat'},
            'European Union': {'avg_temp_c': 12, 'avg_precip_mm': 700, 'primary_crop': 'wheat'},
            'South Asia': {'avg_temp_c': 25, 'avg_precip_mm': 1000, 'primary_crop': 'rice/wheat'},
            'Australia': {'avg_temp_c': 18, 'avg_precip_mm': 450, 'primary_crop': 'wheat'},
            'Sub-Saharan Africa': {'avg_temp_c': 28, 'avg_precip_mm': 800, 'primary_crop': 'maize/sorghum'}
        }

    def generate_temperature_anomaly_scenario(self, region, scenario_type="moderate_warming"):
        """
        Generates hypothetical temperature anomaly data for a given region and scenario.

        Args:
            region (str): The agricultural region (e.g., 'Midwest US', 'Punjab India').
            scenario_type (str): Type of scenario, e.g., "moderate_warming", "extreme_warming".

        Returns:
            dict: A dictionary containing temperature anomaly data.
                  Example: {'region': region, 'scenario': scenario_type, 'temp_increase_c': 2.0}
        """
        if scenario_type == "moderate_warming":
            temp_increase_c = 1.5 # Degrees Celsius
        elif scenario_type == "extreme_warming":
            temp_increase_c = 3.0 # Degrees Celsius
        else:
            temp_increase_c = 1.0 # Default or mild scenario

        return {
            'region': region,
            'scenario': scenario_type,
            'temp_increase_c': temp_increase_c,
            'comment': f"Projected average temperature increase for {region} under {scenario_type}."
        }

    def generate_precipitation_anomaly_scenario(self, region, scenario_type="increased_variability"):
        """
        Generates hypothetical precipitation anomaly data for a given region and scenario.

        Args:
            region (str): The agricultural region.
            scenario_type (str): Type of scenario, e.g., "increased_variability", "prolonged_drought".

        Returns:
            dict: A dictionary containing precipitation anomaly data.
                  Example: {'region': region, 'scenario': scenario_type, 'precip_change_percent': -15, 'pattern': 'more_intense_events'}
        """
        if scenario_type == "increased_variability":
            precip_change_percent = -10 # Percentage change from baseline average
            pattern = "more_intense_events_and_longer_dry_spells"
        elif scenario_type == "prolonged_drought":
            precip_change_percent = -30 # Percentage change
            pattern = "significant_reduction_in seasonal_rainfall"
        else:
            precip_change_percent = 0
            pattern = "no_significant_change_from_baseline"

        return {
            'region': region,
            'scenario': scenario_type,
            'precip_change_percent': precip_change_percent,
            'pattern_description': pattern,
            'comment': f"Projected precipitation changes for {region} under {scenario_type}."
        }

    def correlate_climate_yield_impact(self, temp_anomaly_c, precip_anomaly_percent, region, crop_type="wheat"):
        """
        Correlates climate event characteristics (e.g., temperature rise, rainfall deficit)
        with potential yield impacts for a specific crop and region.
        This is a simplified model based on general research findings.

        Args:
            temp_anomaly_c (float): Temperature anomaly in degrees Celsius (e.g., 2.0 for +2C).
            precip_anomaly_percent (float): Precipitation anomaly in percent (e.g., -20 for 20% deficit).
            region (str): The agricultural region.
            crop_type (str): The type of crop (e.g., 'wheat', 'corn', 'rice').

        Returns:
            dict: An estimated yield impact.
                  Example: {'region': region, 'crop': crop_type, 'temp_impact_percent': -12.0,
                            'precip_impact_percent': -5.0, 'total_estimated_yield_impact_percent': -17.0,
                            'confidence': 'medium', 'notes': 'Based on generalized model.'}
        """
        notes = ["General model: Assumes -6% yield per +1C for wheat globally.",
                 "Precipitation impact is highly variable and region-specific."]
        confidence = "low-to-medium" # Acknowledging simplification

        # Temperature Impact (general rule for wheat, can be adjusted for other crops)
        if crop_type.lower() == 'wheat':
            temp_yield_impact_percent = temp_anomaly_c * -6.0
        elif crop_type.lower() == 'corn':
            temp_yield_impact_percent = temp_anomaly_c * -5.0 # Placeholder
        elif crop_type.lower() == 'rice':
            temp_yield_impact_percent = temp_anomaly_c * -4.0 # Placeholder
        else:
            temp_yield_impact_percent = temp_anomaly_c * -5.0 # Generic placeholder

        # Precipitation Impact (highly simplified)
        # Positive precip anomaly might be good up to a point, then bad (flooding).
        # Negative precip anomaly is generally bad (drought).
        precip_yield_impact_percent = 0
        if precip_anomaly_percent < -10: # Drought conditions
            precip_yield_impact_percent = precip_anomaly_percent * 0.5 # e.g., -20% precip -> -10% yield impact
            notes.append(f"Significant drought conditions ({precip_anomaly_percent}%) likely reduce yield.")
        elif precip_anomaly_percent > 30: # Potential flooding/excessive moisture
             precip_yield_impact_percent = (precip_anomaly_percent - 30) * -0.3 # e.g., +50% precip -> (20 * -0.3) = -6% impact
             notes.append(f"Excessive precipitation ({precip_anomaly_percent}%) may lead to losses.")


        # Regional sensitivity (conceptual placeholder)
        regional_sensitivity_factor = 1.0
        if region in ['South Asia', 'Sub-Saharan Africa']: # Potentially more vulnerable
            regional_sensitivity_factor = 1.2
            notes.append(f"Region {region} considered more sensitive to climate variations.")
        elif region in ['European Union']: # Potentially more resilient due to adaptive capacity
            regional_sensitivity_factor = 0.8
            notes.append(f"Region {region} may have higher adaptive capacity.")

        total_estimated_yield_impact_percent = (temp_yield_impact_percent + precip_yield_impact_percent) * regional_sensitivity_factor

        # Cap the negative impact to avoid unrealistic numbers from simple multiplication
        total_estimated_yield_impact_percent = max(total_estimated_yield_impact_percent, -75.0)


        return {
            'region': region,
            'crop': crop_type,
            'temperature_anomaly_c': temp_anomaly_c,
            'precipitation_anomaly_percent': precip_anomaly_percent,
            'temp_driven_yield_impact_percent': round(temp_yield_impact_percent, 2),
            'precip_driven_yield_impact_percent': round(precip_yield_impact_percent, 2),
            'regional_sensitivity_factor_applied': regional_sensitivity_factor,
            'total_estimated_yield_impact_percent': round(total_estimated_yield_impact_percent, 2),
            'confidence': confidence,
            'notes': notes
        }

class DroughtPropagationTracker:
    def track_drought_across_regions(self, regions: list[str]):
        """
        Track drought propagation across major production regions.
        - Black Sea drought transmission to North Africa import costs
        - North American drought impact on Latin American food security
        - Australian drought effect on Southeast Asian feed markets
        - Brazilian dry spell consequences for Chinese soybean pricing
        - Multi-breadbasket failure scenario stress testing
        """
        pass

class YieldTechnologyAdaptation:
    def project_effectiveness(self, technology_type: str, region: str):
        """
        Project yield technology adaptation effectiveness.
        - Drought-resistant variety penetration rates by region
        - Irrigation technology adoption trajectory
        - Climate-smart agriculture practice diffusion
        - Precision agriculture impact on yield stability
        - Crop diversification strategy effectiveness
        """
        pass

class PriceVolatilityTransmission:
    def simulate_mechanics(self, crop: str, anomaly_type: str):
        """
        Simulate price volatility transmission mechanics.
        - Futures market response curve to production anomalies
        - Physical premium development in deficit regions
        - Substitution elasticity between competing crops
        - Storage and release behavior under scarcity
        - Policy intervention threshold identification
        """
        pass 

class ExtremeTemperatureImpact:
    """
    Assesses the impact of extreme temperature events (heatwaves, frost) on crop yields.
    """

    def __init__(self, crop_susceptibility_data=None):
        """
        Initializes the ExtremeTemperatureImpact assessor.

        Args:
            crop_susceptibility_data (dict, optional): Data on crop susceptibility to heat/frost.
                                                    Example: {'wheat': {'heat_threshold_c': 30, 'frost_threshold_c': -2}}
        """
        self.crop_susceptibility_data = crop_susceptibility_data if crop_susceptibility_data else {
            'wheat': {'heat_threshold_c': 32, 'heat_impact_factor': 0.05, 'frost_threshold_c': -1, 'frost_impact_factor': 0.03},
            'corn': {'heat_threshold_c': 35, 'heat_impact_factor': 0.06, 'frost_threshold_c': 0, 'frost_impact_factor': 0.04}, # Susceptible to late frost
            'rice': {'heat_threshold_c': 35, 'heat_impact_factor': 0.04, 'frost_threshold_c': 5, 'frost_impact_factor': 0.02}, # Generally not frost tolerant
            'soybeans': {'heat_threshold_c': 33, 'heat_impact_factor': 0.05, 'frost_threshold_c': -1, 'frost_impact_factor': 0.03}
        }
        # Impact factor: hypothetical yield loss percentage per degree-day above threshold or per frost event.

    def model_heat_stress_yield_reduction(self, region, crop_type, days_above_threshold, avg_temp_above_threshold):
        """
        Models the potential yield reduction due to heat stress.
        Uses a simplified model based on days above a critical temperature threshold and the intensity.

        Args:
            region (str): The agricultural region.
            crop_type (str): The specific crop.
            days_above_threshold (int): Number of days the temperature exceeded the crop's heat threshold.
            avg_temp_above_threshold (float): The average temperature in Celsius on those days above the threshold.

        Returns:
            dict: Estimated yield reduction due to heat stress.
                  Example: {'region': region, 'crop': crop_type, 'heat_stress_yield_reduction_percent': 15.0,
                            'notes': 'Based on 10 days above 32C for wheat.'}
        """
        if crop_type not in self.crop_susceptibility_data:
            return {
                'region': region, 'crop': crop_type, 'heat_stress_yield_reduction_percent': 0,
                'notes': f'No heat susceptibility data for {crop_type}. Assuming no impact.'
            }

        crop_data = self.crop_susceptibility_data[crop_type]
        heat_threshold = crop_data['heat_threshold_c']
        impact_factor = crop_data['heat_impact_factor']

        if avg_temp_above_threshold <= heat_threshold:
            yield_reduction_percent = 0.0
            notes = "Average temperature did not exceed heat threshold."
        else:
            # Simplified: (degrees above threshold) * days * impact_factor
            degrees_exceeding = avg_temp_above_threshold - heat_threshold
            yield_reduction_percent = degrees_exceeding * days_above_threshold * impact_factor * 100 # Convert factor to percentage
            # Cap reduction at a plausible maximum, e.g., 75%
            yield_reduction_percent = min(yield_reduction_percent, 75.0)
            notes = f"Estimated based on {days_above_threshold} days with avg temp of {avg_temp_above_threshold}°C (threshold {heat_threshold}°C)."
            if yield_reduction_percent > 25: # Based on search result of up to 25% or more
                notes += " High impact scenario, potential for significant losses."


        return {
            'region': region,
            'crop': crop_type,
            'days_above_threshold': days_above_threshold,
            'avg_temp_above_threshold_c': avg_temp_above_threshold,
            'crop_heat_threshold_c': heat_threshold,
            'heat_stress_yield_reduction_percent': round(yield_reduction_percent, 2),
            'notes': notes
        }

    def model_frost_damage_yield_loss(self, region, crop_type, frost_events, avg_min_temp_during_frost):
        """
        Models the potential yield loss due to frost damage.

        Args:
            region (str): The agricultural region.
            crop_type (str): The specific crop.
            frost_events (int): Number of significant frost events during critical growth stages.
            avg_min_temp_during_frost (float): Average minimum temperature during these frost events.

        Returns:
            dict: Estimated yield loss due to frost.
                  Example: {'region': region, 'crop': crop_type, 'frost_yield_loss_percent': 5.0}
        """
        if crop_type not in self.crop_susceptibility_data:
            return {
                'region': region, 'crop': crop_type, 'frost_yield_loss_percent': 0,
                'notes': f'No frost susceptibility data for {crop_type}. Assuming no impact.'
            }

        crop_data = self.crop_susceptibility_data[crop_type]
        frost_threshold = crop_data['frost_threshold_c']
        impact_factor = crop_data['frost_impact_factor']

        yield_loss_percent = 0.0
        notes = ""

        if frost_events > 0 and avg_min_temp_during_frost < frost_threshold:
            # Simplified: severity (degrees below threshold) * events * impact_factor
            degrees_below_frost = frost_threshold - avg_min_temp_during_frost
            yield_loss_percent = degrees_below_frost * frost_events * impact_factor * 100 # Convert factor to percentage
            yield_loss_percent = min(yield_loss_percent, 60.0) # Cap plausible max loss from frost
            notes = f"Estimated based on {frost_events} frost events with avg min temp of {avg_min_temp_during_frost}°C (threshold {frost_threshold}°C)."
        elif frost_events > 0:
            notes = f"{frost_events} frost events reported, but average minimum temperature ({avg_min_temp_during_frost}°C) was not below threshold ({frost_threshold}°C)."
        else:
            notes = "No frost events reported."

        return {
            'region': region,
            'crop': crop_type,
            'frost_events': frost_events,
            'avg_min_temp_during_frost_c': avg_min_temp_during_frost,
            'crop_frost_threshold_c': frost_threshold,
            'frost_yield_loss_percent': round(yield_loss_percent, 2),
            'notes': notes
        } 

class DroughtImpactAssessment:
    """
    Assesses the impact of drought conditions on agricultural yields and recovery times.
    """

    def __init__(self, crop_drought_tolerance=None):
        """
        Initializes the DroughtImpactAssessment.

        Args:
            crop_drought_tolerance (dict, optional): Data on crop tolerance to drought.
                                                    Example: {'wheat': {'critical_water_deficit_percent': 30, 'yield_loss_factor': 0.7}}
        """
        self.crop_drought_tolerance = crop_drought_tolerance if crop_drought_tolerance else {
            'wheat': {'critical_water_deficit_percent': 25, 'yield_loss_factor_per_10_percent_deficit': 0.15, 'max_yield_loss_percent': 70},
            'corn': {'critical_water_deficit_percent': 20, 'yield_loss_factor_per_10_percent_deficit': 0.20, 'max_yield_loss_percent': 80},
            'sorghum': {'critical_water_deficit_percent': 35, 'yield_loss_factor_per_10_percent_deficit': 0.10, 'max_yield_loss_percent': 60},
            'rice': {'critical_water_deficit_percent': 15, 'yield_loss_factor_per_10_percent_deficit': 0.25, 'max_yield_loss_percent': 75} # Assuming irrigated, so deficit is critical
        }
        # yield_loss_factor_per_10_percent_deficit: e.g., for wheat, a 10% water deficit beyond critical might cause 15% yield loss.

    def model_drought_severity_yield_loss(self, region, crop_type, water_deficit_percent, drought_duration_weeks):
        """
        Models yield loss based on drought severity (water deficit) and duration.

        Args:
            region (str): The agricultural region.
            crop_type (str): The specific crop.
            water_deficit_percent (float): The percentage of water deficit compared to normal requirements
                                         during the drought period (e.g., 40 for 40% deficit).
            drought_duration_weeks (int): The duration of the significant drought period in weeks.

        Returns:
            dict: Estimated yield loss due to drought.
                  Example: {'region': region, 'crop': crop_type, 'drought_yield_loss_percent': 25.0}
        """
        if crop_type not in self.crop_drought_tolerance:
            return {
                'region': region, 'crop': crop_type, 'drought_yield_loss_percent': 0,
                'notes': f'No drought tolerance data for {crop_type}. Assuming no impact.'
            }

        crop_data = self.crop_drought_tolerance[crop_type]
        critical_deficit = crop_data['critical_water_deficit_percent']
        loss_factor = crop_data['yield_loss_factor_per_10_percent_deficit']
        max_loss = crop_data['max_yield_loss_percent']

        yield_loss_percent = 0.0
        notes = []

        if water_deficit_percent > critical_deficit:
            effective_deficit = water_deficit_percent - critical_deficit
            # Calculate loss based on how many 10% deficit increments occurred
            loss_increments = effective_deficit / 10.0
            base_yield_loss = loss_increments * loss_factor * 100 # Factor is per 10% deficit, convert to total %

            # Duration can exacerbate the loss (simplified multiplier)
            duration_multiplier = 1.0
            if drought_duration_weeks > 4: # Short drought
                duration_multiplier = 1.0 + (drought_duration_weeks - 4) * 0.05 # Increase impact by 5% per week over 4 weeks
                duration_multiplier = min(duration_multiplier, 1.5) # Cap duration impact
                notes.append(f"Drought duration of {drought_duration_weeks} weeks amplified loss.")
            else:
                notes.append(f"Drought duration: {drought_duration_weeks} weeks.")

            yield_loss_percent = min(base_yield_loss * duration_multiplier, max_loss)
            notes.insert(0, f"Water deficit of {water_deficit_percent}% exceeded critical threshold of {critical_deficit}% for {crop_type}. Calculated base loss: {base_yield_loss:.2f}%.")
        else:
            notes.append(f"Water deficit of {water_deficit_percent}% did not exceed critical threshold of {critical_deficit}% for {crop_type}.")

        return {
            'region': region,
            'crop': crop_type,
            'water_deficit_percent': water_deficit_percent,
            'drought_duration_weeks': drought_duration_weeks,
            'critical_water_deficit_for_crop_percent': critical_deficit,
            'drought_yield_loss_percent': round(yield_loss_percent, 2),
            'notes': "; ".join(notes)
        }

    def simulate_drought_recovery_timescales(self, region, last_drought_severity_index, post_drought_conditions):
        """
        Simulates potential recovery timescales for agricultural land post-drought.

        Args:
            region (str): The agricultural region.
            last_drought_severity_index (float): An index from 0-1 representing severity (1 = very severe).
            post_drought_conditions (str): Description of conditions after drought (e.g., 'normal_rainfall', 'continued_dry').

        Returns:
            dict: Estimated recovery information.
                  Example: {'region': region, 'estimated_recovery_months': 6, 'confidence': 'low',
                            'factors': ['Severity of last drought', 'Post-drought rainfall']}
        """
        estimated_recovery_months = 0
        confidence = "low"
        factors = ["Severity of last drought", "Post-drought rainfall", "Soil health", "Investment in recovery"]

        # Simplified model
        if last_drought_severity_index > 0.8: # Very severe
            estimated_recovery_months = 12 # Base for very severe
            if post_drought_conditions == 'normal_rainfall':
                estimated_recovery_months -= 3
            elif post_drought_conditions == 'continued_dry':
                estimated_recovery_months += 6
                confidence = "very low"
            confidence = "medium" if post_drought_conditions == 'normal_rainfall' else "low"
        elif last_drought_severity_index > 0.5: # Severe
            estimated_recovery_months = 6
            if post_drought_conditions == 'normal_rainfall':
                estimated_recovery_months -= 2
            elif post_drought_conditions == 'continued_dry':
                estimated_recovery_months += 4
            confidence = "medium"
        else: # Moderate or mild
            estimated_recovery_months = 3
            if post_drought_conditions == 'continued_dry':
                estimated_recovery_months += 2
            confidence = "high"

        # Cap recovery time
        estimated_recovery_months = min(max(estimated_recovery_months, 1), 36) # 1 to 36 months range

        return {
            'region': region,
            'last_drought_severity_index (0-1)': last_drought_severity_index,
            'post_drought_conditions': post_drought_conditions,
            'estimated_full_yield_recovery_months': estimated_recovery_months,
            'confidence': confidence,
            'contributing_factors': factors,
            'notes': "Recovery depends heavily on sustained favorable conditions and interventions."
        } 

class FloodImpactAssessment:
    """
    Assesses the impact of flooding events on crop yields and infrastructure.
    """

    def __init__(self, crop_flood_tolerance=None, infrastructure_vulnerability=None):
        """
        Initializes the FloodImpactAssessment.

        Args:
            crop_flood_tolerance (dict, optional): Data on crop tolerance to flooding.
                                                Example: {'rice': {'max_submergence_days': 7, 'loss_factor_per_day': 0.1}}
            infrastructure_vulnerability (dict, optional): Data on infrastructure vulnerability to floods.
        """
        self.crop_flood_tolerance = crop_flood_tolerance if crop_flood_tolerance else {
            'wheat': {'max_submergence_days': 3, 'yield_loss_factor_per_day_submerged': 0.20, 'max_yield_loss_percent': 90},
            'corn': {'max_submergence_days': 4, 'yield_loss_factor_per_day_submerged': 0.15, 'max_yield_loss_percent': 85},
            'soybeans': {'max_submergence_days': 5, 'yield_loss_factor_per_day_submerged': 0.12, 'max_yield_loss_percent': 80},
            'rice': {'max_submergence_days': 10, 'yield_loss_factor_per_day_submerged': 0.08, 'max_yield_loss_percent': 60} # Some varieties are flood tolerant
        }
        self.infrastructure_vulnerability = infrastructure_vulnerability if infrastructure_vulnerability else {
            'rural_roads': {'damage_threshold_flood_depth_m': 0.5, 'repair_cost_per_km_factor': 5000, 'disruption_days_per_event': 7},
            'storage_facilities': {'damage_threshold_flood_depth_m': 0.3, 'content_loss_factor': 0.2, 'repair_time_weeks': 4},
            'irrigation_systems': {'damage_threshold_flood_depth_m': 0.7, 'repair_cost_per_hectare_factor': 300, 'function_loss_months': 2}
        }

    def model_flood_duration_yield_loss(self, region, crop_type, flood_duration_days, water_logging_level):
        """
        Models yield loss based on flood duration and water logging level.

        Args:
            region (str): The agricultural region.
            crop_type (str): The specific crop.
            flood_duration_days (int): Duration of significant water submergence in days.
            water_logging_level (str): Qualitative level, e.g., 'low', 'moderate', 'severe'.

        Returns:
            dict: Estimated yield loss due to flooding.
                  Example: {'region': region, 'crop': crop_type, 'flood_yield_loss_percent': 40.0}
        """
        if crop_type not in self.crop_flood_tolerance:
            return {
                'region': region, 'crop': crop_type, 'flood_yield_loss_percent': 0,
                'notes': f'No flood tolerance data for {crop_type}. Assuming no impact.'
            }

        crop_data = self.crop_flood_tolerance[crop_type]
        max_submergence = crop_data['max_submergence_days']
        loss_factor = crop_data['yield_loss_factor_per_day_submerged']
        max_loss = crop_data['max_yield_loss_percent']

        yield_loss_percent = 0.0
        notes = [f"Water logging level: {water_logging_level}."]

        if flood_duration_days > 0:
            # Base loss on duration
            base_yield_loss = flood_duration_days * loss_factor * 100 # Factor is per day, convert to total %

            # Adjust for severity based on water_logging_level (conceptual)
            severity_multiplier = 1.0
            if water_logging_level == 'severe':
                severity_multiplier = 1.5
                notes.append("Severe water logging likely exacerbated losses.")
            elif water_logging_level == 'moderate':
                severity_multiplier = 1.2
                notes.append("Moderate water logging contributed to losses.")

            yield_loss_percent = min(base_yield_loss * severity_multiplier, max_loss)

            if flood_duration_days > max_submergence:
                yield_loss_percent = max(yield_loss_percent, max_loss * 0.8) # Ensure high loss if max submergence exceeded significantly
                notes.append(f"Flood duration of {flood_duration_days} days exceeded crop's max submergence tolerance of {max_submergence} days.")
            notes.insert(1, f"Calculated base loss for {flood_duration_days} days submerged: {base_yield_loss:.2f}%.")
        else:
            notes.append("No significant flood duration reported.")

        return {
            'region': region,
            'crop': crop_type,
            'flood_duration_days': flood_duration_days,
            'water_logging_level': water_logging_level,
            'crop_max_submergence_days': max_submergence,
            'flood_yield_loss_percent': round(yield_loss_percent, 2),
            'notes': "; ".join(notes)
        }

    def assess_infrastructure_damage_impact(self, region, flood_depth_m, infrastructure_type):
        """
        Assesses the impact of flooding on agricultural infrastructure.

        Args:
            region (str): The agricultural region.
            flood_depth_m (float): Maximum flood water depth in meters.
            infrastructure_type (str): Type of infrastructure (e.g., 'rural_roads', 'storage_facilities').

        Returns:
            dict: Estimated damage and disruption.
                  Example: {'region': region, 'infrastructure': 'rural_roads', 'damage_level': 'moderate',
                            'estimated_repair_cost': 50000, 'disruption_days': 14}
        """
        if infrastructure_type not in self.infrastructure_vulnerability:
            return {
                'region': region, 'infrastructure': infrastructure_type, 'damage_level': 'unknown',
                'notes': f'No vulnerability data for {infrastructure_type}.'
            }

        infra_data = self.infrastructure_vulnerability[infrastructure_type]
        damage_threshold = infra_data['damage_threshold_flood_depth_m']

        damage_level = 'low'
        estimated_repair_cost = 0
        disruption_impact = "minimal"
        notes = [f"Flood depth recorded: {flood_depth_m}m."]

        if flood_depth_m > damage_threshold:
            damage_level = 'moderate'
            if flood_depth_m > damage_threshold * 2: # Arbitrary severe threshold
                damage_level = 'severe'

            # Simplified cost and disruption estimation
            if 'repair_cost_per_km_factor' in infra_data: # For roads
                estimated_repair_cost = infra_data['repair_cost_per_km_factor'] * (flood_depth_m / damage_threshold) * 10 # Assume 10km affected for example
                disruption_impact = f"{infra_data['disruption_days_per_event'] * (flood_depth_m / damage_threshold):.0f} days of disruption for affected routes."
            elif 'content_loss_factor' in infra_data: # For storage
                estimated_repair_cost = 50000 * (flood_depth_m / damage_threshold) # Placeholder repair cost
                content_loss_estimate = infra_data['content_loss_factor'] * 100
                disruption_impact = f"Potential {content_loss_estimate:.0f}% content loss. Repair time: {infra_data['repair_time_weeks']} weeks."
            elif 'repair_cost_per_hectare_factor' in infra_data: # For irrigation
                estimated_repair_cost = infra_data['repair_cost_per_hectare_factor'] * (flood_depth_m / damage_threshold) * 100 # Assume 100ha affected
                disruption_impact = f"Functional loss for {infra_data['function_loss_months']} months."
            else:
                estimated_repair_cost = 20000 * (flood_depth_m / damage_threshold) # Generic cost
                disruption_impact = "Significant operational disruption expected."

            notes.append(f"Damage threshold of {damage_threshold}m exceeded. Estimated damage: {damage_level}.")
        else:
            notes.append(f"Flood depth did not exceed damage threshold of {damage_threshold}m for {infrastructure_type}.")

        return {
            'region': region,
            'infrastructure_type': infrastructure_type,
            'flood_depth_m': flood_depth_m,
            'damage_threshold_m': damage_threshold,
            'estimated_damage_level': damage_level,
            'estimated_repair_cost_usd': round(estimated_repair_cost, 2),
            'estimated_disruption_impact': disruption_impact,
            'notes': "; ".join(notes)
        } 

class ClimateShockYieldVolatility:
    """
    Main class to simulate and analyze the impacts of climate shocks on agricultural yield volatility.
    This class will orchestrate various sub-models for different climate perils.
    """

    def __init__(self, regions, crops, baseline_yield_data=None):
        """
        Initializes the ClimateShockYieldVolatility simulator.

        Args:
            regions (list): List of regions to be included in the simulation.
            crops (list): List of crops to be considered.
            baseline_yield_data (dict, optional): Baseline yield data for region-crop pairs.
                                                 Example: {('North America Plains', 'wheat'): 3.5} (tons/ha)
        """
        self.regions = regions
        self.crops = crops
        self.baseline_yield_data = baseline_yield_data if baseline_yield_data else {
            ('North America Plains', 'wheat'): 3.5, ('European Union', 'wheat'): 5.0,
            ('South Asia', 'rice'): 4.0, ('South Asia', 'wheat'): 3.0,
            ('Australia', 'wheat'): 2.0, ('Sub-Saharan Africa', 'maize'): 1.5
        }

        self.climate_volatility_model = ClimateVolatilityModel()
        self.drought_assessor = DroughtImpactAssessment()
        self.flood_assessor = FloodImpactAssessment()
        self.extreme_temp_assessor = ExtremeTemperatureImpact()

        # Placeholder for more complex propagation models
        self.yield_shock_propagation_model = YieldShockPropagation()


    def simulate_yield_shock_scenarios(self, scenario_name, scenario_parameters):
        """
        Simulates yield shock scenarios based on defined climate parameters.
        This method will call underlying models for specific perils.

        Args:
            scenario_name (str): Name of the scenario (e.g., "SevereDroughtIndia2024", "EUHeatwave2025").
            scenario_parameters (dict): Parameters defining the climate shock.
                Example for drought:
                {
                    'type': 'drought', 'region': 'South Asia', 'crop': 'rice',
                    'water_deficit_percent': 50, 'duration_weeks': 8,
                    'temp_anomaly_c': 2.5, 'precip_anomaly_percent': -50
                }
                Example for heatwave:
                {
                    'type': 'heatwave', 'region': 'European Union', 'crop': 'wheat',
                    'days_above_threshold': 15, 'avg_temp_above_threshold': 35,
                    'temp_anomaly_c': 3.0, 'precip_anomaly_percent': -10
                }
                 Example for general climate change:
                {
                    'type': 'general_climate_change', 'region': 'North America Plains', 'crop': 'wheat',
                    'temp_anomaly_c': 2.0, 'precip_anomaly_percent': -15
                }


        Returns:
            dict: Aggregated results of the yield shock simulation.
                  Includes overall yield impact, contributions from different perils.
        """
        results = {
            'scenario_name': scenario_name,
            'parameters': scenario_parameters,
            'impacts': []
        }
        region = scenario_parameters.get('region')
        crop = scenario_parameters.get('crop')
        shock_type = scenario_parameters.get('type', 'general_climate_change').lower()

        if not region or not crop:
            results['error'] = "Region and crop must be specified in scenario_parameters."
            return results

        temp_anomaly_c = scenario_parameters.get('temp_anomaly_c', 0)
        precip_anomaly_percent = scenario_parameters.get('precip_anomaly_percent', 0)

        # 1. General climate impact (temperature & precipitation trends)
        general_climate_impact = self.climate_volatility_model.correlate_climate_yield_impact(
            temp_anomaly_c=temp_anomaly_c,
            precip_anomaly_percent=precip_anomaly_percent,
            region=region,
            crop_type=crop
        )
        results['impacts'].append({'peril': 'general_climate_trends', 'details': general_climate_impact})
        total_impact_percent = general_climate_impact.get('total_estimated_yield_impact_percent', 0)

        # 2. Specific peril impacts
        if shock_type == 'drought':
            drought_impact = self.drought_assessor.model_drought_severity_yield_loss(
                region=region, crop_type=crop,
                water_deficit_percent=scenario_parameters.get('water_deficit_percent', precip_anomaly_percent * -1 if precip_anomaly_percent < 0 else 0), # Use precip if specific deficit not given
                drought_duration_weeks=scenario_parameters.get('duration_weeks', 4)
            )
            results['impacts'].append({'peril': 'drought', 'details': drought_impact})
            # This specific peril impact might be additive or overriding the general trend for the duration.
            # For simplicity, let's assume it's an additional specific stressor for now.
            # A more complex model would integrate these better.
            total_impact_percent += drought_impact.get('drought_yield_loss_percent', 0)


        elif shock_type == 'heatwave':
            heat_impact = self.extreme_temp_assessor.model_heat_stress_yield_reduction(
                region=region, crop_type=crop,
                days_above_threshold=scenario_parameters.get('days_above_threshold', 0),
                avg_temp_above_threshold=scenario_parameters.get('avg_temp_above_threshold', 0)
            )
            results['impacts'].append({'peril': 'heatwave', 'details': heat_impact})
            total_impact_percent += heat_impact.get('heat_stress_yield_reduction_percent', 0)

        elif shock_type == 'flood':
            flood_impact = self.flood_assessor.model_flood_duration_yield_loss(
                region=region, crop_type=crop,
                flood_duration_days=scenario_parameters.get('flood_duration_days', 0),
                water_logging_level=scenario_parameters.get('water_logging_level', 'moderate')
            )
            results['impacts'].append({'peril': 'flood', 'details': flood_impact})
            total_impact_percent += flood_impact.get('flood_yield_loss_percent', 0)

        elif shock_type == 'frost':
            frost_impact = self.extreme_temp_assessor.model_frost_damage_yield_loss(
                region=region, crop_type=crop,
                frost_events=scenario_parameters.get('frost_events', 0),
                avg_min_temp_during_frost=scenario_parameters.get('avg_min_temp_during_frost', 0)
            )
            results['impacts'].append({'peril': 'frost', 'details': frost_impact})
            total_impact_percent += frost_impact.get('frost_yield_loss_percent', 0)

        # Ensure total impact is capped (e.g., at -100% for total loss)
        results['total_estimated_yield_impact_percent'] = max(total_impact_percent, -100.0)
        
        baseline_yield = self.baseline_yield_data.get((region, crop), None)
        if baseline_yield:
            results['baseline_yield_tons_per_ha'] = baseline_yield
            results['projected_yield_tons_per_ha'] = round(baseline_yield * (1 + results['total_estimated_yield_impact_percent'] / 100.0), 2)
            if results['projected_yield_tons_per_ha'] < 0:
                 results['projected_yield_tons_per_ha'] = 0


        # Placeholder for propagation analysis
        propagation_analysis = self.yield_shock_propagation_model.analyze_supply_chain_impact(
            region=region,
            crop=crop,
            yield_reduction_percentage=results['total_estimated_yield_impact_percent']
        )
        results['supply_chain_propagation_notes'] = propagation_analysis

        return results

    def analyze_regional_impact_multi_shock(self, region, crop, shock_event_timeline):
        """
        Analyzes the cumulative impact of multiple shock events over a timeline in a specific region for a crop.

        Args:
            region (str): The agricultural region.
            crop (str): The crop type.
            shock_event_timeline (list): A list of shock event dicts, each similar to scenario_parameters
                                         in simulate_yield_shock_scenarios, but with a 'year' or 'time_period'.
                                         Example: [{'year': 1, 'type': 'drought', ...}, {'year': 2, 'type': 'heatwave', ...}]

        Returns:
            dict: Aggregated impact analysis for the region and crop over the timeline.
        """
        regional_impact_summary = {
            'region': region,
            'crop': crop,
            'timeline_analysis': [],
            'cumulative_notes': []
        }
        current_yield_modifier = 0.0 # Starts at 0% change

        for event in shock_event_timeline:
            event_params = event.copy()
            event_params['region'] = region # Ensure region and crop are set for the event
            event_params['crop'] = crop
            
            # Adjust temp_anomaly and precip_anomaly for current yield state if needed (complex)
            # For now, assume direct impact of event parameters

            shock_result = self.simulate_yield_shock_scenarios(
                scenario_name=f"{event.get('type', 'event')} in {event.get('year', 'period')}",
                scenario_parameters=event_params
            )
            
            event_impact_percent = shock_result.get('total_estimated_yield_impact_percent',0)
            current_yield_modifier += event_impact_percent # Simplified cumulative for now
            current_yield_modifier = max(current_yield_modifier, -100.0) # Cap at -100%

            event_summary = {
                'period': event.get('year') or event.get('time_period', 'N/A'),
                'event_type': event.get('type'),
                'parameters': event,
                'immediate_impact_percent': event_impact_percent,
                'cumulative_yield_modifier_after_event_percent': current_yield_modifier,
                'details': shock_result['impacts']
            }
            regional_impact_summary['timeline_analysis'].append(event_summary)

        baseline = self.baseline_yield_data.get((region, crop), "N/A")
        regional_impact_summary['baseline_yield_tons_per_ha'] = baseline
        if isinstance(baseline, (int,float)) and regional_impact_summary['timeline_analysis']:
            final_modifier = regional_impact_summary['timeline_analysis'][-1]['cumulative_yield_modifier_after_event_percent']
            regional_impact_summary['final_projected_yield_tons_per_ha'] = round(baseline * (1 + final_modifier / 100.0), 2)
            if regional_impact_summary['final_projected_yield_tons_per_ha'] < 0:
                regional_impact_summary['final_projected_yield_tons_per_ha'] = 0


        regional_impact_summary['cumulative_notes'].append("Simplified cumulative impact. Recovery and adaptation not fully modeled here.")
        return regional_impact_summary

    def model_volatility_propagation(self, initial_shock_region, initial_shock_crop, yield_reduction_percent):
        """
        Models how an initial yield shock in one region/crop might propagate
        through trade, prices, and supply chains. (High-level conceptual call)

        Args:
            initial_shock_region (str): Region of the initial shock.
            initial_shock_crop (str): Crop affected by the initial shock.
            yield_reduction_percent (float): The percentage yield reduction from the shock.

        Returns:
            dict: Analysis of potential propagation effects.
        """
        # This would involve more complex economic modeling, trade flow data, etc.
        # For now, it calls the placeholder YieldShockPropagation model.
        propagation_analysis = self.yield_shock_propagation_model.analyze_cross_regional_impact(
            source_region=initial_shock_region,
            affected_crop=initial_shock_crop,
            source_yield_reduction_percent=yield_reduction_percent
        )
        return {
            'initial_shock': {
                'region': initial_shock_region,
                'crop': initial_shock_crop,
                'yield_reduction_percent': yield_reduction_percent
            },
            'propagation_analysis': propagation_analysis,
            'notes': "This model is conceptual and relies on the YieldShockPropagation sub-model's capabilities."
        }

# Ensure other classes (YieldShockPropagation, ClimateVolatilityModel, etc.) are defined above or imported.
# The following are the updated sub-models, assuming they are correctly placed in the file by previous edits.
# class YieldShockPropagation: ... (already exists with placeholders)
# class ClimateVolatilityModel: ... (updated)
# class DroughtImpactAssessment: ... (updated)
# class FloodImpactAssessment: ... (updated)
# class ExtremeTemperatureImpact: ... (updated)

# [Ensure no further comments or class definitions beyond this point for ClimateShockYieldVolatility]
