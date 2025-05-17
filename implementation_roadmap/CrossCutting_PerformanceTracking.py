class CrossCuttingPerformanceTracking:
    """
    Defines the framework for tracking performance, measuring success,
    and reporting on the progress of the implementation roadmap across all phases.
    This is a continuous activity, not a standalone phase.
    """

    def __init__(self):
        """
        Initializes the CrossCuttingPerformanceTracking.
        """
        pass

    def define_tracking_objectives(self):
        """
        Outlines the core objectives of the performance tracking framework.

        Returns:
            list: A list of strings, where each string is a key objective.
                  Example: ["Monitor progress against roadmap timelines",
                            "Track achievement of strategic and operational KPIs",
                            "Provide timely insights for decision-making"]
        """
        return [
            "Monitor progress of initiatives against planned timelines and budgets.",
            "Track the achievement of strategic objectives and key performance indicators (KPIs).",
            "Measure the impact and ROI of implemented changes and new service offerings.",
            "Provide timely and accurate performance data to stakeholders for informed decision-making.",
            "Identify deviations, risks, and issues early to enable corrective actions.",
            "Ensure accountability for results at all levels.",
            "Facilitate a culture of continuous improvement based on performance insights."
        ]

    def identify_key_performance_indicators(self, initiative_type):
        """
        Identifies relevant KPIs based on the type of initiative or phase.

        Args:
            initiative_type (str): The type of initiative (e.g., 'capability_building',
                                   'service_offering_pilot', 'market_expansion', 'overall_transformation').

        Returns:
            dict: A dictionary of KPIs relevant to the initiative type.
                  Example for 'service_offering_pilot':
                  {'client_satisfaction_score': 'Target >8/10',
                   'project_profitability': 'Target X%',
                   'team_feedback_score': 'Target >4/5'}
        """
        kpis = {
            "common": {
                "initiative_completion_rate": "% of planned tasks/milestones completed on time",
                "budget_variance": "Actual vs. Planned spend",
                "stakeholder_satisfaction_index": "Periodic survey scores from key stakeholders"
            },
            "strategic_prioritization_phase": {
                "clarity_of_priorities_score": "Leadership survey on clarity and buy-in",
                "time_to_finalize_priorities": "Duration of Phase 1"
            },
            "capability_building_phase": {
                "training_completion_rate": "% of targeted employees trained",
                "skill_proficiency_level": "Post-training assessment scores",
                "time_to_deploy_new_system": "Lead time for technology implementation",
                "partnership_activation_rate": "% of planned partnerships operational"
            },
            "pilot_execution_phase": {
                "pilot_project_success_rate": "% of pilots meeting predefined success criteria",
                "client_feedback_on_pilot": "Qualitative and quantitative feedback scores",
                "solution_effectiveness_rating": "Assessment of how well the pilot solution met objectives",
                "cost_of_delivery_pilot": "Cost analysis of pilot engagements"
            },
            "scale_up_rollout_phase": {
                "new_offering_revenue_growth": "Month-over-month or quarter-over-quarter growth",
                "market_share_gain": "% increase in market share for targeted segments",
                "client_acquisition_rate": "Number of new clients for new offerings",
                "employee_adoption_of_new_processes": "% of employees consistently using new tools/SOPs",
                "roi_of_new_initiatives": "Return on Investment calculated for scaled initiatives"
            },
            "overall_transformation_program": {
                "overall_strategic_goals_achievement": "Progress towards overarching strategic goals",
                "consulting_firm_growth_rate": "Year-over-year revenue growth",
                "consulting_firm_profitability": "Overall profit margins",
                "employee_engagement_score": "Firm-wide survey results",
                "client_retention_rate": "Percentage of repeat clients"
            }
        }
        return {**kpis.get("common", {}), **kpis.get(initiative_type, {"error": "Invalid initiative type for KPIs"})}

    def establish_reporting_framework(self):
        """
        Defines the structure, frequency, and audience for performance reporting.

        Returns:
            dict: A dictionary outlining the reporting framework.
                  Example: {'report_types': ['Weekly Progress Update', 'Monthly KPI Dashboard', 'Quarterly Strategic Review'],
                            'audiences': ['Project Teams', 'Steering Committee', 'Executive Leadership'],
                            'key_metrics_per_report': {'Weekly': ['Task completion'], 'Monthly': ['KPIs vs. Target']}}
        """
        return {
            "report_types_frequency": {
                "operational_progress_huddle": "Daily/Weekly (for project teams)",
                "initiative_status_report": "Bi-Weekly/Monthly (for initiative leads, PMO)",
                "kpi_dashboard_review": "Monthly (for functional managers, steering committee)",
                "strategic_performance_review": "Quarterly (for executive leadership, board)"
            },
            "key_content_per_report_type": {
                "operational_progress_huddle": ["Tasks completed", "Upcoming tasks", "Roadblocks/Issues"],
                "initiative_status_report": ["Milestone achievement", "Budget tracking", "Risk status", "Key decisions needed"],
                "kpi_dashboard_review": ["Performance against key KPIs", "Trend analysis", "Variance explanations"],
                "strategic_performance_review": ["Progress towards strategic objectives", "Market impact", "ROI analysis", "Strategic adjustments"]
            },
            "distribution_channels": ["Dedicated performance tracking platform/tool", "Email distribution", "Presentations in review meetings"],
            "responsible_personnel": ["PMO/Performance Analyst", "Initiative Leads", "Finance Department for ROI"]
        }

    def define_review_and_adjustment_process(self):
        """
        Outlines the process for reviewing performance data and making necessary adjustments.

        Returns:
            list: A list of strings describing the review and adjustment cycle.
                  Example: ["Regular performance review meetings",
                            "Root cause analysis for deviations",
                            "Action planning for corrective measures"]
        """
        return [
            "Schedule and conduct regular performance review meetings at different levels (team, management, executive).",
            "Analyze performance data to identify trends, successes, and areas of concern.",
            "Perform root cause analysis for significant deviations from targets or plans.",
            "Develop and prioritize corrective actions or adjustments to strategies/plans.",
            "Assign ownership and timelines for implementing corrective actions.",
            "Track the implementation and effectiveness of corrective actions.",
            "Communicate changes and adjustments to relevant stakeholders.",
            "Incorporate lessons learned into future planning and execution cycles."
        ]

if __name__ == '__main__':
    pt = CrossCuttingPerformanceTracking()
    print("Cross-Cutting: Performance Tracking")
    print("-------------------------------------")
    print("Tracking Objectives:", pt.define_tracking_objectives())
    print("\nKPIs for 'pilot_execution_phase':", pt.identify_key_performance_indicators('pilot_execution_phase'))
    print("KPIs for 'overall_transformation_program':", pt.identify_key_performance_indicators('overall_transformation_program'))
    print("\nReporting Framework:", pt.establish_reporting_framework())
    print("\nReview and Adjustment Process:", pt.define_review_and_adjustment_process()) 