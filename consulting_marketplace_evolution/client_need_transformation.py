# This module will cover the transformation of client needs. 

class ClientPriorityEvolution:
    def __init__(self):
        self.priority_areas = {
            "Climate Risk Assessment and Mitigation": {
                "current_importance_score": 8, # Scale of 1-10
                "trend_outlook": "Rapidly Increasing", # Increasing, Stable, Decreasing
                "drivers": ["Extreme weather events", "Regulatory pressures (e.g., carbon reporting)", 
                            "Investor expectations", "Impact on yield and operational stability"],
                "consulting_needs": ["Climate vulnerability assessments", "Adaptation strategy development", 
                                   "Decarbonization roadmaps", "Climate-resilient supply chain design"]
            },
            "Supply Chain Resilience Enhancement": {
                "current_importance_score": 9,
                "trend_outlook": "Rapidly Increasing",
                "drivers": ["Geopolitical disruptions", "Port congestions & logistic bottlenecks", 
                            "Pandemic-induced vulnerabilities", "Climate change impacts on production hubs"],
                "consulting_needs": ["Supply chain mapping & risk analysis", "Sourcing diversification strategies", 
                                   "Inventory optimization models", "Contingency planning & crisis response"]
            },
            "Sustainability Transformation Support (ESG Integration)": {
                "current_importance_score": 7,
                "trend_outlook": "Increasing",
                "drivers": ["Consumer demand for sustainable products", "Regulatory requirements (e.g., EU Green Deal)", 
                            "Access to capital (green finance)", "Brand reputation & corporate responsibility"],
                "consulting_needs": ["ESG strategy development & implementation", "Sustainable sourcing programs", 
                                   "Carbon accounting & footprint reduction", "Circular economy initiatives", "Regenerative agriculture transition support"]
            },
            "Market Access Strategy Development & Diversification": {
                "current_importance_score": 7,
                "trend_outlook": "Increasing",
                "drivers": ["Trade policy volatility & protectionism", "Emerging market growth opportunities", 
                            "Shifting consumer preferences (e.g., plant-based)", "Need to reduce reliance on single markets"],
                "consulting_needs": ["New market entry analysis", "Trade barrier navigation", 
                                   "Value chain analysis for new product categories", "Export readiness assessment"]
            },
            "Digital Transformation Enablement": {
                "current_importance_score": 8,
                "trend_outlook": "Rapidly Increasing",
                "drivers": ["Need for operational efficiency & cost reduction", "Data-driven decision making", 
                            "Adoption of precision agriculture", "Improved traceability & transparency demands"],
                "consulting_needs": ["Digital strategy & roadmap development", "Technology selection & implementation (ERP, IoT, AI)", 
                                   "Data analytics & business intelligence solutions", "Change management for digital adoption"]
            }
        }

    def model_evolution(self, priority_area: str, years_to_project: int = 5) -> dict:
        """
        Models the evolution of a client priority area over a number of years.
        This is a simplified model; a real one would use more complex forecasting.
        """
        if priority_area not in self.priority_areas:
            return {"error": f"Priority area '{priority_area}' not recognized."}

        current_data = self.priority_areas[priority_area]
        projected_importance_score = current_data["current_importance_score"]
        
        # Simplified projection logic
        if current_data["trend_outlook"] == "Rapidly Increasing":
            projection_factor = 0.3 * years_to_project # Faster increase
        elif current_data["trend_outlook"] == "Increasing":
            projection_factor = 0.15 * years_to_project # Slower increase
        else: # Stable or Decreasing (not modeled to decrease in this simple version)
            projection_factor = 0

        projected_importance_score = min(10, current_data["current_importance_score"] + projection_factor * (10 - current_data["current_importance_score"])/5) # Approach 10, decelerating
        projected_importance_score = round(projected_importance_score, 1)

        return {
            "priority_area": priority_area,
            "current_importance_score": current_data["current_importance_score"],
            "current_trend_outlook": current_data["trend_outlook"],
            "drivers": current_data["drivers"],
            "associated_consulting_needs": current_data["consulting_needs"],
            "projected_importance_score_in_years": projected_importance_score,
            "projection_period_years": years_to_project
        }

    def get_all_priority_details(self):
        """Returns details for all configured priority areas."""
        return self.priority_areas

class DecisionMakerProfileShift:
    def __init__(self):
        self.profiles = {
            "Chief Executive Officer (CEO)": {
                "traditional_focus": ["Overall P&L", "Strategic Growth", "Shareholder Value"],
                "emerging_focus": ["Long-term Resilience", "Sustainability Integration", "Stakeholder Management", "Digital Transformation Vision"],
                "influence_change": "Increasingly involved in sustainability and risk decisions previously delegated.",
                "key_concerns": ["Navigating volatility", "Ensuring supply chain integrity", "Meeting ESG mandates", "Future-proofing the business"],
                "consulting_implications": ["High-level strategy", "Transformation programs", "Risk management frameworks", "Sustainability strategy integration"]
            },
            "Chief Financial Officer (CFO)": {
                "traditional_focus": ["Financial Reporting", "Cost Control", "Capital Allocation"],
                "emerging_focus": ["ESG-linked Finance", "Climate Risk Financial Disclosure", "Investment in Sustainable Assets", "Quantifying Non-Financial Risks"],
                "influence_change": "Growing role in evaluating climate/sustainability investments and risks.",
                "key_concerns": ["Access to capital", "Cost of capital", "Reporting complexity (e.g., TCFD, CSRD)", "ROI of sustainability initiatives"],
                "consulting_implications": ["Sustainable finance advisory", "ESG reporting and assurance", "Climate risk modeling", "Internal carbon pricing"]
            },
            "Chief Operating Officer (COO) / Head of Supply Chain": {
                "traditional_focus": ["Operational Efficiency", "Logistics", "Procurement Costs"],
                "emerging_focus": ["Supply Chain Transparency & Traceability", "Resilience to Shocks (Climate, Geopolitical)", "Decarbonization of Operations", "Ethical Sourcing"],
                "influence_change": "Shift from pure cost focus to resilience and sustainability within operations.",
                "key_concerns": ["Disruptions", "Input cost volatility", "Regulatory compliance in operations", "Labor shortages", "Infrastructure bottlenecks"],
                "consulting_implications": ["Supply chain optimization and diversification", "Traceability system implementation", "Operational decarbonization plans", "Port and logistics strategy"]
            },
            "Chief Sustainability Officer (CSO) / Head of ESG": {
                "traditional_focus": "N/A (often a newer role or combined with other functions)",
                "emerging_focus": ["Developing and implementing ESG strategy", "Stakeholder engagement on sustainability", "Ensuring compliance with ESG regulations", "Driving sustainable innovation"],
                "influence_change": "Rapidly increasing influence, often with direct C-suite reporting lines.",
                "key_concerns": ["Data collection and reporting", "Alignment of sustainability with business strategy", "Resource allocation", "Demonstrating impact"],
                "consulting_implications": ["ESG strategy development", "Materiality assessments", "Impact measurement and reporting", "Sustainability governance"]
            },
            "Head of Trading / Risk Management": {
                "traditional_focus": ["Price Risk Management (Hedging)", "Market Analysis", "Arbitrage"],
                "emerging_focus": ["Carbon Trading/Offsets", "Weather Derivatives", "Managing Long-Tail Climate Risks", "Counterparty Risk from ESG Factors"],
                "influence_change": "Expanding scope of risk management beyond traditional commodity price volatility.",
                "key_concerns": ["Increased market volatility (climate, geopolitical)", "Regulatory changes in derivatives markets", "Liquidity of new environmental markets"],
                "consulting_implications": ["Advanced risk modeling", "Carbon market advisory", "Development of new hedging instruments"]
            },
             "Chief Technology/Information Officer (CTO/CIO)": {
                "traditional_focus": ["IT Infrastructure", "Enterprise Resource Planning (ERP) systems", "Cybersecurity basics"],
                "emerging_focus": ["Digital agriculture platforms", "Data analytics for operational efficiency and sustainability", "AI and ML applications in trading/agronomy", "Enhanced cybersecurity for critical infrastructure"],
                "influence_change": "Elevated role from support function to strategic enabler of business transformation.",
                "key_concerns": ["Data integration and management", "Scalability of new technologies", "ROI on tech investments", "Talent gap for specialized digital skills"],
                "consulting_implications": ["Digital transformation roadmap", "AgTech platform selection and implementation", "Data strategy and governance", "AI/ML solution development"]
            },
            "Head of Government Affairs / Corporate Relations": {
                "traditional_focus": ["Lobbying on trade policy", "Managing corporate reputation"],
                "emerging_focus": ["Navigating complex climate and sustainability regulations", "Engaging on food security policies", "Shaping standards for sustainable agriculture"],
                "influence_change": "Increased importance due to growing regulatory scrutiny and public expectations.",
                "key_concerns": ["Pace and complexity of new regulations", "Maintaining license to operate", "Geopolitical instability impacting policy"],
                "consulting_implications": ["Policy analysis and advocacy strategy", "Stakeholder mapping and engagement", "Reputation risk management related to ESG"]
            }
        }

    def get_profile(self, role_title):
        """
        Retrieves the profile for a specific decision-maker role.
        """
        return self.profiles.get(role_title, {"error": "Role not found"})

    def analyze_shift_impact(self, role_title):
        """
        Provides a qualitative analysis of how a role's shift impacts consulting demand.
        """
        profile = self.get_profile(role_title)
        if "error" in profile:
            return profile["error"]
        
        impact_statement = f"The role of {role_title} is evolving. "
        impact_statement += f"Traditionally focused on {', '.join(profile['traditional_focus'])}, "
        impact_statement += f"their emerging focus includes {', '.join(profile['emerging_focus'])}. "
        impact_statement += f"This shift, driven by concerns like {', '.join(profile['key_concerns'])}, means that consulting services related to {', '.join(profile['consulting_implications'])} are in higher demand for this profile."
        return impact_statement

class ProblemFramingEvolution:
    def __init__(self):
        self.framing_shifts = {
            "Risk Management": {
                "traditional_framing": "Focus on isolated, often short-term financial or operational risks (e.g., price volatility, single-source supply disruption). Solutions are often tactical and siloed.",
                "emerging_framing": "Integrated risk-opportunity assessment across the entire value system. Emphasizes interconnectedness of climate, geopolitical, social, and market risks. Proactive resilience building, scenario planning, and understanding of systemic vulnerabilities. Strong sustainability principles considered (ecological limits).",
                "drivers_of_shift": ["Increased frequency/intensity of systemic shocks (climate, pandemics)", "Investor pressure for ESG risk disclosure", "Recognition of limitations of purely financial hedging"],
                "consulting_implications": ["Holistic enterprise risk management (ERM) frameworks", "Climate scenario analysis and TCFD reporting support", "Supply chain resilience and diversification strategies incorporating systems thinking", "Advisory on 'strong sustainability' metrics and planetary boundaries"]
            },
            "Sustainability & ESG": {
                "traditional_framing": "Often viewed as a compliance issue, CSR reporting, or philanthropic activity, separate from core business. Focus on 'weak sustainability' (balancing economic, social, environmental goals, allowing trade-offs).",
                "emerging_framing": "ESG as a core driver of long-term value creation, resilience, and competitive advantage. Shift towards 'strong sustainability' where economic activities are nested within social and ecological limits. Focus on transformative capacity, regenerative practices, and circular economy models. Requires systems thinking to understand impacts across the value chain and beyond.",
                "drivers_of_shift": ["Regulatory frameworks (EU Green Deal, CSRD)", "Investor demand for robust ESG performance", "Consumer and societal expectations", "Scientific consensus on climate change and biodiversity loss"],
                "consulting_implications": ["Integrated ESG strategy development", "Materiality assessments based on system-wide impacts", "Support for implementing regenerative agriculture and circular models", "Development of metrics for 'transformative capacity' and ecological footprint reduction", "Stakeholder engagement for co-creating solutions"]
            },
            "Value Chain Strategy": {
                "traditional_framing": "Linear 'farm-to-fork' optimization, primarily focused on cost reduction, efficiency, and transactional relationships. Limited consideration of externalities or broader system impacts.",
                "emerging_framing": "Value system/network perspective, recognizing complex interdependencies. Emphasis on collaboration, transparency, and shared value creation. Integration of circularity, resilience, and social equity. Development of 'transformative capacities' among all actors (e.g., smallholders).",
                "drivers_of_shift": ["Demand for traceability and transparency", "Need for greater resilience against disruptions", "Opportunities in new business models (e.g., direct-to-consumer, service models)", "Ethical sourcing and fair labor practice concerns"],
                "consulting_implications": ["Value network mapping and analysis", "Collaborative platform development for data sharing and co-innovation", "Design of inclusive business models focusing on smallholder empowerment", "Support for building 'transformative capacity' within value chains through training and knowledge co-creation"]
            },
            "Innovation & Technology": {
                "traditional_framing": "Technology adoption for point solutions, often focused on incremental improvements in productivity or efficiency. Siloed R&D efforts.",
                "emerging_framing": "Systems innovation approach. Technology as an enabler of broader food system transformation (e.g., digital agriculture for sustainability, AI for risk modeling). Focus on interoperability, data governance, and democratizing access to technology. Co-creation of solutions with diverse stakeholders.",
                "drivers_of_shift": ["Advancements in AI, IoT, biotech, and data analytics", "Urgency to address complex challenges like climate change and food security", "Potential for disruptive innovation from new entrants", "Need for scalable and adaptable solutions"],
                "consulting_implications": ["Food system transformation roadmaps leveraging technology", "Development of digital ecosystems and data platforms", "Advisory on ethical AI and data governance", "Facilitation of multi-stakeholder innovation labs and 'transformative capacity' building for tech adoption"]
            }
        }

    def get_framing_details(self, framing_aspect: str):
        """
        Retrieves details for a specific problem framing aspect.
        """
        return self.framing_shifts.get(framing_aspect, {"error": "Framing aspect not found"})

    def analyze_evolution_impact(self, framing_aspect: str):
        """
        Provides a qualitative analysis of how the evolution of a framing aspect impacts consulting.
        """
        details = self.get_framing_details(framing_aspect)
        if "error" in details:
            return details["error"]

        impact_statement = f"The framing of '{framing_aspect}' is evolving. "
        impact_statement += f"Traditionally, it was seen as: '{details['traditional_framing']}'. "
        impact_statement += f"The emerging framing is: '{details['emerging_framing']}'. "
        impact_statement += f"This shift, driven by factors like {', '.join(details['drivers_of_shift'])}, creates demand for consulting in areas such as: {', '.join(details['consulting_implications'])}."
        return impact_statement

class BudgetAllocationShifts:
    def __init__(self):
        self.allocation_areas = {
            "Traditional Production R&D (e.g., conventional breeding)": {
                "historical_allocation_pct": 15, # Hypothetical percentage of discretionary budget
                "current_trend": "Decreasing/Reallocating",
                "drivers": ["Shift to biotech/digital ag R&D", "Focus on sustainability-linked innovations"],
                "notes": "Investment often integrated into broader sustainability or digital initiatives."
            },
            "Market Expansion & Physical Asset Acquisition": {
                "historical_allocation_pct": 20,
                "current_trend": "Stable but More Selective",
                "drivers": ["Geopolitical risks", "Supply chain resilience focus", "Higher cost of capital"],
                "notes": "Emphasis on acquiring assets that enhance supply chain control or access to sustainable sources."
            },
            "Climate Change Adaptation & Mitigation": {
                "historical_allocation_pct": 5,
                "current_trend": "Rapidly Increasing",
                "drivers": ["Physical risk to assets/supply", "Regulatory mandates", "Investor pressure", "Consumer demand for sustainable products"],
                "notes": "Includes investment in resilient infrastructure, water management, and carbon sequestration projects."
            },
            "Sustainability Initiatives (beyond climate)": {
                "historical_allocation_pct": 7,
                "current_trend": "Increasing",
                "drivers": ["ESG reporting requirements", "Brand reputation", "Access to green finance", "Employee retention"],
                "notes": "Covers biodiversity, waste reduction, ethical sourcing, community engagement."
            },
            "Digital Transformation & Data Analytics": {
                "historical_allocation_pct": 10,
                "current_trend": "Strongly Increasing",
                "drivers": ["Efficiency gains", "Improved decision-making", "Enhanced traceability", "New service offerings"],
                "notes": "Includes investment in ERP systems, AI/ML, IoT, blockchain, and data platforms."
            },
            "Supply Chain Resilience & Diversification": {
                "historical_allocation_pct": 8,
                "current_trend": "Increasing",
                "drivers": ["Geopolitical disruptions", "Climate-related disruptions", "Pandemic lessons"],
                "notes": "Focus on multi-sourcing, regional hubs, and inventory management strategies."
            },
            "Talent Development & Reskilling (for new needs)": {
                "historical_allocation_pct": 5,
                "current_trend": "Increasing",
                "drivers": ["Need for data scientists, sustainability experts, digital skills", "Competition for talent"],
                "notes": "Investment in training programs and attracting new types of professionals."
            }
        }

    def get_allocation_details(self, area_name):
        """Retrieves details for a specific budget allocation area."""
        return self.allocation_areas.get(area_name, {"error": "Area not found."})

    def analyze_overall_shift_trends(self):
        """Provides a summary of major budget allocation shift trends."""
        trends = {}
        for area, details in self.allocation_areas.items():
            trends[area] = details["current_trend"]
        return trends

class SectorBoundaryBlurring:
    def __init__(self):
        self.blurring_examples = {
            "Tech Companies in Agriculture": {
                "players": ["Google (Verily, Mineral)", "Microsoft (Azure FarmBeats)", "Amazon (AWS for Agriculture)", "IBM (Weather Company)"],
                "activities": [
                    "Precision agriculture platforms (data analytics, AI/ML for yield optimization, pest/disease prediction)",
                    "Farm management software (FMS) and ERP systems",
                    "IoT sensor networks and drone imagery analysis",
                    "Cloud computing infrastructure for large-scale data processing",
                    "Development of sustainability monitoring and carbon tracking tools"
                ],
                "impact_on_agribusiness": [
                    "New sources of competition for traditional ag tech providers",
                    "Partnership opportunities for data integration and service delivery",
                    "Acceleration of digital adoption on farms",
                    "Potential for disintermediation of traditional advisors/input sellers if tech offers direct solutions"
                ],
                "consulting_implications": ["Advising ag companies on digital strategy", "Tech partnership brokering", "Change management for digital adoption"]
            },
            "Financial Institutions & Fintech in Agriculture": {
                "players": ["Specialized ag lenders", "Impact investors", "Fintech startups (e.g., focused on farm finance, risk management, carbon markets)"],
                "activities": [
                    "Data-driven credit scoring and loan origination for farmers",
                    "Parametric insurance products (e.g., weather-indexed)",
                    "Platforms for trading agricultural derivatives and managing price risk",
                    "Investment in sustainable agriculture and carbon credit generation",
                    "Supply chain finance solutions"
                ],
                "impact_on_agribusiness": [
                    "New financing options for farmers and agribusinesses",
                    "Increased focus on financial data and traceability for loan/insurance eligibility",
                    "Integration of financial services with farm management platforms"
                ],
                "consulting_implications": ["Advising on fintech partnerships", "Developing new financial products for ag", "Supporting carbon market strategies"]
            },
            "Retail & Consumer Packaged Goods (CPG) Companies Engaging Upstream": {
                "players": ["Large grocery retailers (e.g., Walmart, Tesco)", "Global CPG companies (e.g., Unilever, Nestle, P&G)"],
                "activities": [
                    "Direct sourcing programs with farmers/cooperatives",
                    "Implementing sustainability and traceability standards throughout their supply chains (e.g., for regenerative ag, deforestation-free)",
                    "Investing in supply chain technology (e.g., blockchain for traceability)",
                    "Developing private label brands with specific provenance/sustainability claims",
                    "Engaging in consumer education about food origins and sustainability"
                ],
                "impact_on_agribusiness": [
                    "Increased demand for identity-preserved and sustainably produced commodities",
                    "Pressure on processors and traders to meet retailer/CPG standards",
                    "Opportunities for farmers who can meet these standards (potential for premiums)",
                    "Shift in power dynamics, with downstream players influencing farm-level practices"
                ],
                "consulting_implications": ["Supply chain mapping and assurance", "Sustainability strategy for suppliers", "Connecting farmers to new value chains"]
            },
            "Agribusiness Companies Expanding into New Areas": {
                "players": ["Large grain traders", "Seed/chemical companies", "Equipment manufacturers"],
                "activities": [
                    "Developing proprietary digital farming platforms and data services",
                    "Investing in or acquiring ag tech startups",
                    "Offering risk management and financial services to farmer customers",
                    "Expanding into downstream processing or direct-to-consumer models (less common but emerging)",
                    "Carbon farming program development"
                ],
                "impact_on_agribusiness": [
                    "Increased competition among established players in new service areas",
                    "Efforts to create 'closed-loop' ecosystems around their core offerings",
                    "Potential for data lock-in and interoperability challenges"
                ],
                "consulting_implications": ["Business model innovation", "M&A advisory in ag tech", "Competitive strategy in a converging market"]
            }
        }

    def get_blurring_details(self, sector_example_name):
        """Retrieves details for a specific sector boundary blurring example."""
        return self.blurring_examples.get(sector_example_name, {"error": "Example not found."})

    def analyze_implications_for_client(self, client_type, blurring_example_name):
        """Analyzes the implications of a specific blurring example for a given client type (e.g., 'Grain Trader', 'Input Supplier', 'Farmer Cooperative')."""
        example = self.get_blurring_details(blurring_example_name)
        if "error" in example:
            return example

        implications = example.get("impact_on_agribusiness", [])
        consulting_needs = example.get("consulting_implications", [])
        
        # This is a simplified analysis. A real model would have more nuanced logic.
        specific_implications = f"For a {client_type}, the blurring driven by '{blurring_example_name}' means: "
        specific_implications += ", ".join(implications)
        specific_implications += f". This creates consulting needs around: {', '.join(consulting_needs)}."
        
        return {
            "client_type": client_type,
            "blurring_example": blurring_example_name,
            "general_impacts": implications,
            "general_consulting_needs": consulting_needs,
            "client_specific_summary": specific_implications
        }

class ClientNeedTransformation:
    def __init__(self):
        self.priority_evolution = ClientPriorityEvolution()
        self.decision_maker_shift = DecisionMakerProfileShift()
        self.problem_framing_evolution = ProblemFramingEvolution()
        self.budget_allocation_shifts = BudgetAllocationShifts()
        self.sector_boundary_blurring = SectorBoundaryBlurring()

    def get_comprehensive_client_outlook(self, client_segment, region):
        """
        Provides a comprehensive outlook on client needs transformation
        for a given segment and region.
        """
        print(f"--- Comprehensive Client Outlook for {client_segment} in {region} ---")

        priority_projection_details = self.priority_evolution.model_evolution(
            priority_area="Supply Chain Resilience Enhancement", 
            years_to_project=5
        )
        projected_importance_score = priority_projection_details.get("projected_importance_score_in_years", "N/A")
        print(f"\nProjected Importance for Supply Chain Resilience (5 years): {projected_importance_score}")

        cso_profile = self.decision_maker_shift.get_profile("Chief Sustainability Officer (CSO)")
        print(f"\nCSO Profile Key Concerns: {cso_profile.get('key_concerns', 'N/A')}")

        systemic_framing = self.problem_framing_evolution.get_framing_details("Risk Management")
        print(f"\nEmerging Problem Framing (Risk Management): {systemic_framing.get('emerging_framing', 'N/A')}")

        budget_trends = self.budget_allocation_shifts.analyze_overall_shift_trends()
        print(f"\nOverall Budget Allocation Shift Trends (Top 3):")
        for area, trend in list(budget_trends.items())[:3]:
            print(f"  - {area}: {trend}")
            
        blurring_implications = self.sector_boundary_blurring.analyze_implications_for_client(
            client_type=client_segment, # Using client_segment as a proxy for client_type
            blurring_example_name="Tech Companies in Agriculture"
        )
        print(f"\nImplications of Tech Blurring for {client_segment}: {blurring_implications.get('client_specific_summary', 'N/A')}")

        return {
            "priority_projection": priority_projection_details, # Return the whole dict for more info
            "cso_profile_concerns": cso_profile.get('key_concerns'),
            "systemic_framing_description": systemic_framing.get('emerging_framing'), # Changed from .get('description')
            "budget_trends_sample": dict(list(budget_trends.items())[:3]),
            "blurring_impact_example": blurring_implications
        }

if __name__ == '__main__':
    client_needs_sim = ClientNeedTransformation()

    print("--- Example 1: Comprehensive Client Outlook ---")
    outlook = client_needs_sim.get_comprehensive_client_outlook(
        client_segment="Large Agribusiness",
        region="Global"
    )

    print("\n--- Example 2: Client Priority Evolution Analysis ---")
    priority_details = client_needs_sim.priority_evolution.get_priority_details("Digital Transformation")
    print(f"Details for Digital Transformation Priority: Current Importance {priority_details.get('current_importance_score')}, Trend: {priority_details.get('trend_outlook')}")
    projected_importance = client_needs_sim.priority_evolution.project_priority_importance("Digital Transformation", 3)
    print(f"Projected importance in 3 years: {projected_importance:.2f}")

    print("\n--- Example 3: Decision Maker Profile ---")
    ceo_profile = client_needs_sim.decision_maker_shift.get_profile_details("Chief Executive Officer (CEO)")
    print(f"CEO Emerging Focus: {ceo_profile.get('emerging_focus', 'N/A')}")

    print("\n--- Example 4: Problem Framing Evolution ---")
    risk_framing_details = client_needs_sim.problem_framing_evolution.get_framing_details("Risk Management")
    print(f"Emerging framing for Risk Management: {risk_framing_details.get('emerging_framing', 'N/A')}")

    print("\n--- Example 5: Budget Allocation Shifts ---")
    sustainability_budget = client_needs_sim.budget_allocation_shifts.get_allocation_details("Sustainability Initiatives (beyond climate)")
    print(f"Sustainability Budget Trend: {sustainability_budget.get('current_trend', 'N/A')}, Drivers: {sustainability_budget.get('drivers')}")

    print("\n--- Example 6: Sector Boundary Blurring ---")
    tech_blur_details = client_needs_sim.sector_boundary_blurring.get_blurring_details("Tech Companies in Agriculture")
    print(f"Details of Tech Companies in Agriculture: Players - {tech_blur_details.get('players')}")
    retail_blur_implications = client_needs_sim.sector_boundary_blurring.analyze_implications_for_client(
        client_type="Food Processor", 
        blurring_example_name="Retail & Consumer Packaged Goods (CPG) Companies Engaging Upstream"
    )
    print(f"Implications of Retail/CPG Blurring for Food Processor: {retail_blur_implications.get('client_specific_summary')}")
    agribiz_expansion = client_needs_sim.sector_boundary_blurring.get_blurring_details("Agribusiness Companies Expanding into New Areas")
    print(f"Agribusiness Expansion Activities: {agribiz_expansion.get('activities')}") 