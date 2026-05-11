MOCK_EXPERIMENTS = {
  "EXP_CART_REDESIGN": {
    "name": "Cart Redesign V2",
    "hypothesis": "Simplifying the cart UI will increase checkout conversion by reducing cognitive load",
    "primary_metric": "Checkout Conversion Rate",
    "guardrail_metrics": [
      "Page Load Time",
      "Error Rate",
      "Cart Abandonment Rate"
    ],
    "start_date": "2026-05-01",
    "end_date": "2026-05-15",
    "traffic_split": 50,
    "target_audience": "All Web Users",
    "status": "In Analysis",
    "primary_owner": "Jane Doe - Growth PM",
    "last_updated": "1 days ago",
    "overview": "This experiment aims to validate the business impact of the Cart Redesign V2 initiative. By doing so, we expect to see improvements across our primary metric while monitoring our core guardrails to ensure a safe rollout.",
    "hypothesis_details": {
      "if": "we implement the changes for Cart Redesign V2",
      "then": "we will observe an increase in Checkout Conversion Rate",
      "because": "Simplifying the cart UI will increase checkout conversion by reducing cognitive load"
    },
    "variant_a_desc": "The existing baseline experience without any modifications. Serves as the control for accurate measurement.",
    "variant_b_desc": "The proposed treatment implementing Cart Redesign V2. This variant includes the new design and logic.",
    "power_calc": {
      "baseline_cvr": "2.1%",
      "mde": "+5.0% relative",
      "power": "80%",
      "alpha": "0.05",
      "sample_size": "55,000 per variant",
      "runtime_days": "14"
    },
    "segmentation_plan": [
      {
        "segment": "Mobile vs Desktop",
        "rationale": "UI changes often perform differently across device viewports."
      },
      {
        "segment": "New vs Returning",
        "rationale": "New users lack anchoring bias to the old design."
      },
      {
        "segment": "High vs Low Value",
        "rationale": "Ensure we don't accidentally penalize our most valuable cohort."
      }
    ]
  },
  "EXP_NEW_PRICING": {
    "name": "Quiet Luxury Retail Pricing Test",
    "hypothesis": "IF we increase the checkout price from $39 to $59 for 35% of users, THEN revenue per user will increase by at least 15% BECAUSE our customer base shows low price sensitivity and high willingness to pay for premium quality items based on prior research",
    "primary_metric": "Revenue Per User",
    "guardrail_metrics": [
      "Conversion Rate",
      "Page Load Time",
      "Error Rate"
    ],
    "start_date": "2026-05-01",
    "end_date": "2026-05-15",
    "traffic_split": 35,
    "target_audience": "All Web Users",
    "status": "Under Investigation",
    "primary_owner": "Revenue Growth Team",
    "last_updated": "2 days ago",
    "overview": "ABC Corp. is testing whether raising the subscription price from $39 to $59 increases total revenue per user, despite an expected drop in conversion rate. This test ran across all acquisition channels from March to May 2015.",
    "hypothesis_details": {
      "if": "we increase the subscription price from $39 to $59 for 35% of users",
      "then": "revenue per user will increase by at least 15%",
      "because": "our iOS, Mac, and friend-referral users show low price sensitivity and high willingness to pay based on prior research"
    },
    "variant_a_desc": "Control: User sees $39/month pricing on the checkout page. Standard flow, no changes.",
    "variant_b_desc": "Treatment: User sees $59/month pricing on the checkout page. All other UI elements identical.",
    "power_calc": {
      "baseline_cvr": "1.99%",
      "mde": "33% relative drop (from 1.99% to 1.33%)",
      "power": "80%",
      "alpha": "0.05",
      "sample_size": "5,548 per group",
      "runtime_days": "Less than 1 week at 50% traffic split"
    },
    "segmentation_plan": [
      {
        "segment": "Device (Mobile vs Web)",
        "rationale": "Mobile users expected to be less price sensitive — validate this hypothesis"
      },
      {
        "segment": "Operating System",
        "rationale": "iOS/Mac users typically higher LTV — check if they react differently to price increase"
      },
      {
        "segment": "Acquisition Source",
        "rationale": "Friend referral and paid ads users have different price sensitivity profiles"
      },
      {
        "segment": "Geography (Top 10 Cities)",
        "rationale": "Revenue per user varies significantly by city — check for geographic skew"
      }
    ]
  },
  "EXP_MOCK_1": {
    "name": "Mock Experiment 1",
    "hypothesis": "Hypothesis for mock experiment 1.",
    "primary_metric": "Checkout Conversion Rate",
    "guardrail_metrics": [
      "Page Load Time",
      "Error Rate"
    ],
    "start_date": "2026-06-01",
    "end_date": "2026-06-15",
    "traffic_split": 50,
    "target_audience": "All Users",
    "status": "In Analysis",
    "primary_owner": "Alice Johnson - Monetization",
    "last_updated": "3 days ago",
    "overview": "This experiment aims to validate the business impact of the Mock Experiment 1 initiative. By doing so, we expect to see improvements across our primary metric while monitoring our core guardrails to ensure a safe rollout.",
    "hypothesis_details": {
      "if": "we implement the changes for Mock Experiment 1",
      "then": "we will observe an increase in Checkout Conversion Rate",
      "because": "Hypothesis for mock experiment 1."
    },
    "variant_a_desc": "The existing baseline experience without any modifications. Serves as the control for accurate measurement.",
    "variant_b_desc": "The proposed treatment implementing Mock Experiment 1. This variant includes the new design and logic.",
    "power_calc": {
      "baseline_cvr": "2.1%",
      "mde": "+5.0% relative",
      "power": "80%",
      "alpha": "0.05",
      "sample_size": "55,000 per variant",
      "runtime_days": "14"
    },
    "segmentation_plan": [
      {
        "segment": "Mobile vs Desktop",
        "rationale": "UI changes often perform differently across device viewports."
      },
      {
        "segment": "New vs Returning",
        "rationale": "New users lack anchoring bias to the old design."
      },
      {
        "segment": "High vs Low Value",
        "rationale": "Ensure we don't accidentally penalize our most valuable cohort."
      }
    ]
  },
  "EXP_MOCK_2": {
    "name": "Mock Experiment 2",
    "hypothesis": "Hypothesis for mock experiment 2.",
    "primary_metric": "Checkout Conversion Rate",
    "guardrail_metrics": [
      "Page Load Time",
      "Error Rate"
    ],
    "start_date": "2026-06-01",
    "end_date": "2026-06-15",
    "traffic_split": 50,
    "target_audience": "All Users",
    "status": "In Analysis",
    "primary_owner": "Bob Lee - Core UX",
    "last_updated": "4 days ago",
    "overview": "This experiment aims to validate the business impact of the Mock Experiment 2 initiative. By doing so, we expect to see improvements across our primary metric while monitoring our core guardrails to ensure a safe rollout.",
    "hypothesis_details": {
      "if": "we implement the changes for Mock Experiment 2",
      "then": "we will observe an increase in Checkout Conversion Rate",
      "because": "Hypothesis for mock experiment 2."
    },
    "variant_a_desc": "The existing baseline experience without any modifications. Serves as the control for accurate measurement.",
    "variant_b_desc": "The proposed treatment implementing Mock Experiment 2. This variant includes the new design and logic.",
    "power_calc": {
      "baseline_cvr": "2.1%",
      "mde": "+5.0% relative",
      "power": "80%",
      "alpha": "0.05",
      "sample_size": "55,000 per variant",
      "runtime_days": "14"
    },
    "segmentation_plan": [
      {
        "segment": "Mobile vs Desktop",
        "rationale": "UI changes often perform differently across device viewports."
      },
      {
        "segment": "New vs Returning",
        "rationale": "New users lack anchoring bias to the old design."
      },
      {
        "segment": "High vs Low Value",
        "rationale": "Ensure we don't accidentally penalize our most valuable cohort."
      }
    ]
  },
  "EXP_MOCK_3": {
    "name": "Mock Experiment 3",
    "hypothesis": "Hypothesis for mock experiment 3.",
    "primary_metric": "Checkout Conversion Rate",
    "guardrail_metrics": [
      "Page Load Time",
      "Error Rate"
    ],
    "start_date": "2026-06-01",
    "end_date": "2026-06-15",
    "traffic_split": 50,
    "target_audience": "All Users",
    "status": "In Analysis",
    "primary_owner": "Jane Doe - Growth PM",
    "last_updated": "5 days ago",
    "overview": "This experiment aims to validate the business impact of the Mock Experiment 3 initiative. By doing so, we expect to see improvements across our primary metric while monitoring our core guardrails to ensure a safe rollout.",
    "hypothesis_details": {
      "if": "we implement the changes for Mock Experiment 3",
      "then": "we will observe an increase in Checkout Conversion Rate",
      "because": "Hypothesis for mock experiment 3."
    },
    "variant_a_desc": "The existing baseline experience without any modifications. Serves as the control for accurate measurement.",
    "variant_b_desc": "The proposed treatment implementing Mock Experiment 3. This variant includes the new design and logic.",
    "power_calc": {
      "baseline_cvr": "2.1%",
      "mde": "+5.0% relative",
      "power": "80%",
      "alpha": "0.05",
      "sample_size": "55,000 per variant",
      "runtime_days": "14"
    },
    "segmentation_plan": [
      {
        "segment": "Mobile vs Desktop",
        "rationale": "UI changes often perform differently across device viewports."
      },
      {
        "segment": "New vs Returning",
        "rationale": "New users lack anchoring bias to the old design."
      },
      {
        "segment": "High vs Low Value",
        "rationale": "Ensure we don't accidentally penalize our most valuable cohort."
      }
    ]
  },
  "EXP_MOCK_4": {
    "name": "Mock Experiment 4",
    "hypothesis": "Hypothesis for mock experiment 4.",
    "primary_metric": "Checkout Conversion Rate",
    "guardrail_metrics": [
      "Page Load Time",
      "Error Rate"
    ],
    "start_date": "2026-06-01",
    "end_date": "2026-06-15",
    "traffic_split": 50,
    "target_audience": "All Users",
    "status": "In Analysis",
    "primary_owner": "John Smith - Product",
    "last_updated": "1 days ago",
    "overview": "This experiment aims to validate the business impact of the Mock Experiment 4 initiative. By doing so, we expect to see improvements across our primary metric while monitoring our core guardrails to ensure a safe rollout.",
    "hypothesis_details": {
      "if": "we implement the changes for Mock Experiment 4",
      "then": "we will observe an increase in Checkout Conversion Rate",
      "because": "Hypothesis for mock experiment 4."
    },
    "variant_a_desc": "The existing baseline experience without any modifications. Serves as the control for accurate measurement.",
    "variant_b_desc": "The proposed treatment implementing Mock Experiment 4. This variant includes the new design and logic.",
    "power_calc": {
      "baseline_cvr": "2.1%",
      "mde": "+5.0% relative",
      "power": "80%",
      "alpha": "0.05",
      "sample_size": "55,000 per variant",
      "runtime_days": "14"
    },
    "segmentation_plan": [
      {
        "segment": "Mobile vs Desktop",
        "rationale": "UI changes often perform differently across device viewports."
      },
      {
        "segment": "New vs Returning",
        "rationale": "New users lack anchoring bias to the old design."
      },
      {
        "segment": "High vs Low Value",
        "rationale": "Ensure we don't accidentally penalize our most valuable cohort."
      }
    ]
  },
  "EXP_MOCK_5": {
    "name": "Mock Experiment 5",
    "hypothesis": "Hypothesis for mock experiment 5.",
    "primary_metric": "Checkout Conversion Rate",
    "guardrail_metrics": [
      "Page Load Time",
      "Error Rate"
    ],
    "start_date": "2026-06-01",
    "end_date": "2026-06-15",
    "traffic_split": 50,
    "target_audience": "All Users",
    "status": "In Analysis",
    "primary_owner": "Alice Johnson - Monetization",
    "last_updated": "2 days ago",
    "overview": "This experiment aims to validate the business impact of the Mock Experiment 5 initiative. By doing so, we expect to see improvements across our primary metric while monitoring our core guardrails to ensure a safe rollout.",
    "hypothesis_details": {
      "if": "we implement the changes for Mock Experiment 5",
      "then": "we will observe an increase in Checkout Conversion Rate",
      "because": "Hypothesis for mock experiment 5."
    },
    "variant_a_desc": "The existing baseline experience without any modifications. Serves as the control for accurate measurement.",
    "variant_b_desc": "The proposed treatment implementing Mock Experiment 5. This variant includes the new design and logic.",
    "power_calc": {
      "baseline_cvr": "2.1%",
      "mde": "+5.0% relative",
      "power": "80%",
      "alpha": "0.05",
      "sample_size": "55,000 per variant",
      "runtime_days": "14"
    },
    "segmentation_plan": [
      {
        "segment": "Mobile vs Desktop",
        "rationale": "UI changes often perform differently across device viewports."
      },
      {
        "segment": "New vs Returning",
        "rationale": "New users lack anchoring bias to the old design."
      },
      {
        "segment": "High vs Low Value",
        "rationale": "Ensure we don't accidentally penalize our most valuable cohort."
      }
    ]
  },
  "EXP_MOCK_6": {
    "name": "Mock Experiment 6",
    "hypothesis": "Hypothesis for mock experiment 6.",
    "primary_metric": "Checkout Conversion Rate",
    "guardrail_metrics": [
      "Page Load Time",
      "Error Rate"
    ],
    "start_date": "2026-06-01",
    "end_date": "2026-06-15",
    "traffic_split": 50,
    "target_audience": "All Users",
    "status": "In Analysis",
    "primary_owner": "Bob Lee - Core UX",
    "last_updated": "3 days ago",
    "overview": "This experiment aims to validate the business impact of the Mock Experiment 6 initiative. By doing so, we expect to see improvements across our primary metric while monitoring our core guardrails to ensure a safe rollout.",
    "hypothesis_details": {
      "if": "we implement the changes for Mock Experiment 6",
      "then": "we will observe an increase in Checkout Conversion Rate",
      "because": "Hypothesis for mock experiment 6."
    },
    "variant_a_desc": "The existing baseline experience without any modifications. Serves as the control for accurate measurement.",
    "variant_b_desc": "The proposed treatment implementing Mock Experiment 6. This variant includes the new design and logic.",
    "power_calc": {
      "baseline_cvr": "2.1%",
      "mde": "+5.0% relative",
      "power": "80%",
      "alpha": "0.05",
      "sample_size": "55,000 per variant",
      "runtime_days": "14"
    },
    "segmentation_plan": [
      {
        "segment": "Mobile vs Desktop",
        "rationale": "UI changes often perform differently across device viewports."
      },
      {
        "segment": "New vs Returning",
        "rationale": "New users lack anchoring bias to the old design."
      },
      {
        "segment": "High vs Low Value",
        "rationale": "Ensure we don't accidentally penalize our most valuable cohort."
      }
    ]
  },
  "EXP_MOCK_7": {
    "name": "Mock Experiment 7",
    "hypothesis": "Hypothesis for mock experiment 7.",
    "primary_metric": "Checkout Conversion Rate",
    "guardrail_metrics": [
      "Page Load Time",
      "Error Rate"
    ],
    "start_date": "2026-06-01",
    "end_date": "2026-06-15",
    "traffic_split": 50,
    "target_audience": "All Users",
    "status": "In Analysis",
    "primary_owner": "Jane Doe - Growth PM",
    "last_updated": "4 days ago",
    "overview": "This experiment aims to validate the business impact of the Mock Experiment 7 initiative. By doing so, we expect to see improvements across our primary metric while monitoring our core guardrails to ensure a safe rollout.",
    "hypothesis_details": {
      "if": "we implement the changes for Mock Experiment 7",
      "then": "we will observe an increase in Checkout Conversion Rate",
      "because": "Hypothesis for mock experiment 7."
    },
    "variant_a_desc": "The existing baseline experience without any modifications. Serves as the control for accurate measurement.",
    "variant_b_desc": "The proposed treatment implementing Mock Experiment 7. This variant includes the new design and logic.",
    "power_calc": {
      "baseline_cvr": "2.1%",
      "mde": "+5.0% relative",
      "power": "80%",
      "alpha": "0.05",
      "sample_size": "55,000 per variant",
      "runtime_days": "14"
    },
    "segmentation_plan": [
      {
        "segment": "Mobile vs Desktop",
        "rationale": "UI changes often perform differently across device viewports."
      },
      {
        "segment": "New vs Returning",
        "rationale": "New users lack anchoring bias to the old design."
      },
      {
        "segment": "High vs Low Value",
        "rationale": "Ensure we don't accidentally penalize our most valuable cohort."
      }
    ]
  },
  "EXP_MOCK_8": {
    "name": "Mock Experiment 8",
    "hypothesis": "Hypothesis for mock experiment 8.",
    "primary_metric": "Checkout Conversion Rate",
    "guardrail_metrics": [
      "Page Load Time",
      "Error Rate"
    ],
    "start_date": "2026-06-01",
    "end_date": "2026-06-15",
    "traffic_split": 50,
    "target_audience": "All Users",
    "status": "In Analysis",
    "primary_owner": "John Smith - Product",
    "last_updated": "5 days ago",
    "overview": "This experiment aims to validate the business impact of the Mock Experiment 8 initiative. By doing so, we expect to see improvements across our primary metric while monitoring our core guardrails to ensure a safe rollout.",
    "hypothesis_details": {
      "if": "we implement the changes for Mock Experiment 8",
      "then": "we will observe an increase in Checkout Conversion Rate",
      "because": "Hypothesis for mock experiment 8."
    },
    "variant_a_desc": "The existing baseline experience without any modifications. Serves as the control for accurate measurement.",
    "variant_b_desc": "The proposed treatment implementing Mock Experiment 8. This variant includes the new design and logic.",
    "power_calc": {
      "baseline_cvr": "2.1%",
      "mde": "+5.0% relative",
      "power": "80%",
      "alpha": "0.05",
      "sample_size": "55,000 per variant",
      "runtime_days": "14"
    },
    "segmentation_plan": [
      {
        "segment": "Mobile vs Desktop",
        "rationale": "UI changes often perform differently across device viewports."
      },
      {
        "segment": "New vs Returning",
        "rationale": "New users lack anchoring bias to the old design."
      },
      {
        "segment": "High vs Low Value",
        "rationale": "Ensure we don't accidentally penalize our most valuable cohort."
      }
    ]
  },
  "EXP_MOCK_9": {
    "name": "Mock Experiment 9",
    "hypothesis": "Hypothesis for mock experiment 9.",
    "primary_metric": "Checkout Conversion Rate",
    "guardrail_metrics": [
      "Page Load Time",
      "Error Rate"
    ],
    "start_date": "2026-06-01",
    "end_date": "2026-06-15",
    "traffic_split": 50,
    "target_audience": "All Users",
    "status": "In Analysis",
    "primary_owner": "Alice Johnson - Monetization",
    "last_updated": "1 days ago",
    "overview": "This experiment aims to validate the business impact of the Mock Experiment 9 initiative. By doing so, we expect to see improvements across our primary metric while monitoring our core guardrails to ensure a safe rollout.",
    "hypothesis_details": {
      "if": "we implement the changes for Mock Experiment 9",
      "then": "we will observe an increase in Checkout Conversion Rate",
      "because": "Hypothesis for mock experiment 9."
    },
    "variant_a_desc": "The existing baseline experience without any modifications. Serves as the control for accurate measurement.",
    "variant_b_desc": "The proposed treatment implementing Mock Experiment 9. This variant includes the new design and logic.",
    "power_calc": {
      "baseline_cvr": "2.1%",
      "mde": "+5.0% relative",
      "power": "80%",
      "alpha": "0.05",
      "sample_size": "55,000 per variant",
      "runtime_days": "14"
    },
    "segmentation_plan": [
      {
        "segment": "Mobile vs Desktop",
        "rationale": "UI changes often perform differently across device viewports."
      },
      {
        "segment": "New vs Returning",
        "rationale": "New users lack anchoring bias to the old design."
      },
      {
        "segment": "High vs Low Value",
        "rationale": "Ensure we don't accidentally penalize our most valuable cohort."
      }
    ]
  },
  "EXP_MOCK_10": {
    "name": "Mock Experiment 10",
    "hypothesis": "Hypothesis for mock experiment 10.",
    "primary_metric": "Checkout Conversion Rate",
    "guardrail_metrics": [
      "Page Load Time",
      "Error Rate"
    ],
    "start_date": "2026-06-01",
    "end_date": "2026-06-15",
    "traffic_split": 50,
    "target_audience": "All Users",
    "status": "In Analysis",
    "primary_owner": "Bob Lee - Core UX",
    "last_updated": "2 days ago",
    "overview": "This experiment aims to validate the business impact of the Mock Experiment 10 initiative. By doing so, we expect to see improvements across our primary metric while monitoring our core guardrails to ensure a safe rollout.",
    "hypothesis_details": {
      "if": "we implement the changes for Mock Experiment 10",
      "then": "we will observe an increase in Checkout Conversion Rate",
      "because": "Hypothesis for mock experiment 10."
    },
    "variant_a_desc": "The existing baseline experience without any modifications. Serves as the control for accurate measurement.",
    "variant_b_desc": "The proposed treatment implementing Mock Experiment 10. This variant includes the new design and logic.",
    "power_calc": {
      "baseline_cvr": "2.1%",
      "mde": "+5.0% relative",
      "power": "80%",
      "alpha": "0.05",
      "sample_size": "55,000 per variant",
      "runtime_days": "14"
    },
    "segmentation_plan": [
      {
        "segment": "Mobile vs Desktop",
        "rationale": "UI changes often perform differently across device viewports."
      },
      {
        "segment": "New vs Returning",
        "rationale": "New users lack anchoring bias to the old design."
      },
      {
        "segment": "High vs Low Value",
        "rationale": "Ensure we don't accidentally penalize our most valuable cohort."
      }
    ]
  }
}


MOCK_METRICS = {
  "EXP_CART_REDESIGN": {
    "control": {
      "sessions": 150000,
      "conversions": 3000,
      "conversion_rate": 0.02,
      "revenue": 150000,
      "aov": 50.0
    },
    "treatment": {
      "sessions": 151000,
      "conversions": 3450,
      "conversion_rate": 0.0228,
      "revenue": 175000,
      "aov": 50.72
    }
  },
  "EXP_NEW_PRICING": {
    "control": {
      "sessions": 148000,
      "conversions": 2960,
      "conversion_rate": 0.02,
      "revenue": 148000,
      "aov": 50.0
    },
    "treatment": {
      "sessions": 155000,
      "conversions": 2945,
      "conversion_rate": 0.019,
      "revenue": 178000,
      "aov": 60.44
    }
  },
  "EXP_MOCK_1": {
    "control": {
      "sessions": 105000,
      "conversions": 2100,
      "conversion_rate": 0.02,
      "revenue": 105000,
      "aov": 50.0
    },
    "treatment": {
      "sessions": 105100,
      "conversions": 2154,
      "conversion_rate": 0.0205,
      "revenue": 109854,
      "aov": 51.0
    }
  },
  "EXP_MOCK_2": {
    "control": {
      "sessions": 110000,
      "conversions": 2200,
      "conversion_rate": 0.02,
      "revenue": 110000,
      "aov": 50.0
    },
    "treatment": {
      "sessions": 110200,
      "conversions": 2314,
      "conversion_rate": 0.021,
      "revenue": 120328,
      "aov": 52.0
    }
  },
  "EXP_MOCK_3": {
    "control": {
      "sessions": 115000,
      "conversions": 2300,
      "conversion_rate": 0.02,
      "revenue": 115000,
      "aov": 50.0
    },
    "treatment": {
      "sessions": 115300,
      "conversions": 2478,
      "conversion_rate": 0.0215,
      "revenue": 131334,
      "aov": 53.0
    }
  },
  "EXP_MOCK_4": {
    "control": {
      "sessions": 120000,
      "conversions": 2400,
      "conversion_rate": 0.02,
      "revenue": 120000,
      "aov": 50.0
    },
    "treatment": {
      "sessions": 120400,
      "conversions": 2648,
      "conversion_rate": 0.022,
      "revenue": 142992,
      "aov": 54.0
    }
  },
  "EXP_MOCK_5": {
    "control": {
      "sessions": 125000,
      "conversions": 2500,
      "conversion_rate": 0.02,
      "revenue": 125000,
      "aov": 50.0
    },
    "treatment": {
      "sessions": 125500,
      "conversions": 2823,
      "conversion_rate": 0.0225,
      "revenue": 155265,
      "aov": 55.0
    }
  },
  "EXP_MOCK_6": {
    "control": {
      "sessions": 130000,
      "conversions": 2600,
      "conversion_rate": 0.02,
      "revenue": 130000,
      "aov": 50.0
    },
    "treatment": {
      "sessions": 130600,
      "conversions": 3003,
      "conversion_rate": 0.023,
      "revenue": 168168,
      "aov": 56.0
    }
  },
  "EXP_MOCK_7": {
    "control": {
      "sessions": 135000,
      "conversions": 2700,
      "conversion_rate": 0.02,
      "revenue": 135000,
      "aov": 50.0
    },
    "treatment": {
      "sessions": 135700,
      "conversions": 3188,
      "conversion_rate": 0.0235,
      "revenue": 181716,
      "aov": 57.0
    }
  },
  "EXP_MOCK_8": {
    "control": {
      "sessions": 140000,
      "conversions": 2800,
      "conversion_rate": 0.02,
      "revenue": 140000,
      "aov": 50.0
    },
    "treatment": {
      "sessions": 140800,
      "conversions": 3379,
      "conversion_rate": 0.024,
      "revenue": 195982,
      "aov": 58.0
    }
  },
  "EXP_MOCK_9": {
    "control": {
      "sessions": 145000,
      "conversions": 2900,
      "conversion_rate": 0.02,
      "revenue": 145000,
      "aov": 50.0
    },
    "treatment": {
      "sessions": 145900,
      "conversions": 3574,
      "conversion_rate": 0.0245,
      "revenue": 210866,
      "aov": 59.0
    }
  },
  "EXP_MOCK_10": {
    "control": {
      "sessions": 150000,
      "conversions": 3000,
      "conversion_rate": 0.02,
      "revenue": 150000,
      "aov": 50.0
    },
    "treatment": {
      "sessions": 151000,
      "conversions": 3775,
      "conversion_rate": 0.025,
      "revenue": 226500,
      "aov": 60.0
    }
  }
}

MOCK_CUPED = {
  "EXP_CART_REDESIGN": {
    "p_value": 0.001,
    "ci_lower": 0.018,
    "ci_upper": 0.066,
    "variance_reduction": 42,
    "significant": True,
    "srm": False
  },
  "EXP_NEW_PRICING": {
    "p_value": 0.21,
    "ci_lower": -0.031,
    "ci_upper": 0.052,
    "variance_reduction": 18,
    "significant": False,
    "srm": True
  },
  "EXP_MOCK_1": {
    "p_value": 0.45,
    "ci_lower": -0.01,
    "ci_upper": 0.05,
    "variance_reduction": 21,
    "significant": False,
    "srm": False
  },
  "EXP_MOCK_2": {
    "p_value": 0.01,
    "ci_lower": -0.01,
    "ci_upper": 0.05,
    "variance_reduction": 22,
    "significant": True,
    "srm": False
  },
  "EXP_MOCK_3": {
    "p_value": 0.45,
    "ci_lower": -0.01,
    "ci_upper": 0.05,
    "variance_reduction": 23,
    "significant": False,
    "srm": False
  },
  "EXP_MOCK_4": {
    "p_value": 0.01,
    "ci_lower": -0.01,
    "ci_upper": 0.05,
    "variance_reduction": 24,
    "significant": True,
    "srm": False
  },
  "EXP_MOCK_5": {
    "p_value": 0.45,
    "ci_lower": -0.01,
    "ci_upper": 0.05,
    "variance_reduction": 25,
    "significant": False,
    "srm": False
  },
  "EXP_MOCK_6": {
    "p_value": 0.01,
    "ci_lower": -0.01,
    "ci_upper": 0.05,
    "variance_reduction": 26,
    "significant": True,
    "srm": False
  },
  "EXP_MOCK_7": {
    "p_value": 0.45,
    "ci_lower": -0.01,
    "ci_upper": 0.05,
    "variance_reduction": 27,
    "significant": False,
    "srm": False
  },
  "EXP_MOCK_8": {
    "p_value": 0.01,
    "ci_lower": -0.01,
    "ci_upper": 0.05,
    "variance_reduction": 28,
    "significant": True,
    "srm": False
  },
  "EXP_MOCK_9": {
    "p_value": 0.45,
    "ci_lower": -0.01,
    "ci_upper": 0.05,
    "variance_reduction": 29,
    "significant": False,
    "srm": False
  },
  "EXP_MOCK_10": {
    "p_value": 0.01,
    "ci_lower": -0.01,
    "ci_upper": 0.05,
    "variance_reduction": 30,
    "significant": True,
    "srm": False
  }
}

MOCK_SEGMENTS = {
  "EXP_CART_REDESIGN": [
    {
      "segment": "Mobile",
      "lift": "+12.1%",
      "p_value": 0.003,
      "warning": None
    },
    {
      "segment": "Desktop",
      "lift": "+15.8%",
      "p_value": 0.001,
      "warning": None
    },
    {
      "segment": "New Users",
      "lift": "+18.2%",
      "p_value": 0.001,
      "warning": None
    },
    {
      "segment": "Returning",
      "lift": "+10.4%",
      "p_value": 0.008,
      "warning": None
    }
  ],
  "EXP_NEW_PRICING": [
    {
      "segment": "Mobile",
      "lift": "-8.3%",
      "p_value": 0.002,
      "warning": "SIMPSON PARADOX: Overall positive but Mobile hurt"
    },
    {
      "segment": "Desktop",
      "lift": "+22.4%",
      "p_value": 0.001,
      "warning": None
    },
    {
      "segment": "New Users",
      "lift": "+5.1%",
      "p_value": 0.18,
      "warning": None
    },
    {
      "segment": "Returning",
      "lift": "+19.7%",
      "p_value": 0.001,
      "warning": None
    }
  ],
  "EXP_MOCK_1": [
    {
      "segment": "Mobile",
      "lift": "+1%",
      "p_value": 0.45,
      "warning": None
    },
    {
      "segment": "Desktop",
      "lift": "+3%",
      "p_value": 0.01,
      "warning": None
    }
  ],
  "EXP_MOCK_2": [
    {
      "segment": "Mobile",
      "lift": "+2%",
      "p_value": 0.01,
      "warning": None
    },
    {
      "segment": "Desktop",
      "lift": "+4%",
      "p_value": 0.01,
      "warning": None
    }
  ],
  "EXP_MOCK_3": [
    {
      "segment": "Mobile",
      "lift": "+3%",
      "p_value": 0.45,
      "warning": None
    },
    {
      "segment": "Desktop",
      "lift": "+5%",
      "p_value": 0.01,
      "warning": None
    }
  ],
  "EXP_MOCK_4": [
    {
      "segment": "Mobile",
      "lift": "+4%",
      "p_value": 0.01,
      "warning": None
    },
    {
      "segment": "Desktop",
      "lift": "+6%",
      "p_value": 0.01,
      "warning": None
    }
  ],
  "EXP_MOCK_5": [
    {
      "segment": "Mobile",
      "lift": "+5%",
      "p_value": 0.45,
      "warning": None
    },
    {
      "segment": "Desktop",
      "lift": "+7%",
      "p_value": 0.01,
      "warning": None
    }
  ],
  "EXP_MOCK_6": [
    {
      "segment": "Mobile",
      "lift": "+6%",
      "p_value": 0.01,
      "warning": None
    },
    {
      "segment": "Desktop",
      "lift": "+8%",
      "p_value": 0.01,
      "warning": None
    }
  ],
  "EXP_MOCK_7": [
    {
      "segment": "Mobile",
      "lift": "+7%",
      "p_value": 0.45,
      "warning": None
    },
    {
      "segment": "Desktop",
      "lift": "+9%",
      "p_value": 0.01,
      "warning": None
    }
  ],
  "EXP_MOCK_8": [
    {
      "segment": "Mobile",
      "lift": "+8%",
      "p_value": 0.01,
      "warning": None
    },
    {
      "segment": "Desktop",
      "lift": "+10%",
      "p_value": 0.01,
      "warning": None
    }
  ],
  "EXP_MOCK_9": [
    {
      "segment": "Mobile",
      "lift": "+9%",
      "p_value": 0.45,
      "warning": None
    },
    {
      "segment": "Desktop",
      "lift": "+11%",
      "p_value": 0.01,
      "warning": None
    }
  ],
  "EXP_MOCK_10": [
    {
      "segment": "Mobile",
      "lift": "+10%",
      "p_value": 0.01,
      "warning": None
    },
    {
      "segment": "Desktop",
      "lift": "+12%",
      "p_value": 0.01,
      "warning": None
    }
  ]
}

# MOCK_RAG_STORE and MOCK_POST_ANALYSIS_CODE remain unchanged.
# I'll just append them from the original file.

MOCK_RAG_STORE = [
  {
    "id": "RAG_001",
    "title": "Q3 2025: Cart CTA Button Color Test — Validated",
    "summary": "Simplifying cart UI showed +9% lift but a novelty effect in week 1 inflated results. Recommend 2-week minimum runtime."
  },
  {
    "id": "RAG_002",
    "title": "Q1 2026: Checkout Flow Redesign — Novelty Effect Confirmed",
    "summary": "Flow redesign showed -3% in week 1, recovered to +11% by week 2. Always check time-series before concluding."
  },
  {
    "id": "RAG_003",
    "title": "Q4 2025: Dynamic Pricing Pilot — Mobile Segment Alert",
    "summary": "Pricing changes consistently hurt mobile users due to smaller screen price anchoring. Flag mobile as guardrail for any pricing test."
  }
]

MOCK_POST_ANALYSIS_CODE = {
  "traffic": """
import pandas as pd
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
import io, base64

# CTE 1: sessions_by_day — get daily session counts per variant
data = {'day': list(range(1,15))*2,
        'variant': ['Control']*14 + ['Treatment']*14,
        'sessions': [10500+i*20 for i in range(14)] + 
                    [10600+i*22 for i in range(14)]}
df = pd.DataFrame(data)

# CTE 2: pivot — reshape for plotting
pivot = df.pivot(index='day', columns='variant', values='sessions')

fig, ax = plt.subplots(figsize=(9, 4))
pivot.plot(ax=ax, marker='o')
ax.set_title('Daily Sessions by Variant')
ax.set_xlabel('Day of Experiment')
ax.set_ylabel('Sessions')
ax.legend()
plt.tight_layout()

buf = io.BytesIO()
plt.savefig(buf, format='png', bbox_inches='tight')
buf.seek(0)
img_b64 = base64.b64encode(buf.read()).decode('utf-8')
img_b64
""",
  "novelty": """
import pandas as pd
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
import io, base64

# CTE 1: daily_conversion — compute daily CVR per variant
data = {'day': list(range(1,15))*2,
        'variant': ['Control']*14 + ['Treatment']*14,
        'cvr': [0.020]*14 + 
               [0.015,0.016,0.018,0.020,0.021,0.022,0.022,
                0.023,0.023,0.024,0.024,0.025,0.025,0.025]}
df = pd.DataFrame(data)

# CTE 2: pivot for plotting
pivot = df.pivot(index='day', columns='variant', values='cvr')

fig, ax = plt.subplots(figsize=(9, 4))
pivot.plot(ax=ax, marker='o')
ax.axvline(x=7, color='red', linestyle='--', 
           label='Novelty Effect Boundary (Day 7)')
ax.set_title('Daily Conversion Rate — Novelty Effect Check')
ax.set_xlabel('Day')
ax.set_ylabel('Conversion Rate')
ax.legend()
plt.tight_layout()

buf = io.BytesIO()
plt.savefig(buf, format='png', bbox_inches='tight')
buf.seek(0)
img_b64 = base64.b64encode(buf.read()).decode('utf-8')
img_b64
""",
  "source_x_axis": """
import pandas as pd, matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
import io, base64

# Step 1: Revenue per user by source and variant (Vertical Chart)
data = {
    'source': ['friend_referral','ads_facebook',
               'ads-google','seo-google',
               'direct_traffic','ads-bing',
               'ads-yahoo','seo_facebook',
               'ads_other','seo-yahoo'],
    'control_rev': [1.82,0.89,0.91,0.78,
                    0.71,0.68,0.65,0.72,0.61,0.55],
    'treatment_rev': [2.31,1.14,1.18,0.98,
                      0.89,0.84,0.79,0.88,0.71,0.61]
}
df = pd.DataFrame(data).sort_values('treatment_rev', ascending=False)

fig, ax = plt.subplots(figsize=(10,5))
x = range(len(df))
ax.bar([i-0.2 for i in x], df['control_rev'], 
        width=0.4, label='Control ($39)', 
        color='#94a3b8')
ax.bar([i+0.2 for i in x], df['treatment_rev'], 
        width=0.4, label='Treatment ($59)', 
        color='#3b82f6')
ax.set_xticks(list(x))
ax.set_xticklabels(df['source'], rotation=45, ha='right')
ax.set_ylabel('Avg Revenue Per User ($)')
ax.set_title('Revenue Per User by Acquisition Source')
ax.legend()
plt.tight_layout()

buf = io.BytesIO()
plt.savefig(buf, format='png', bbox_inches='tight')
buf.seek(0)
img_b64 = base64.b64encode(buf.read()).decode('utf-8')
img_b64
""",
  "source": """
import pandas as pd, matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
import io, base64

# Step 1: Revenue per user by source and variant
data = {
    'source': ['friend_referral','ads_facebook',
               'ads-google','seo-google',
               'direct_traffic','ads-bing',
               'ads-yahoo','seo_facebook',
               'ads_other','seo-yahoo'],
    'control_rev': [1.82,0.89,0.91,0.78,
                    0.71,0.68,0.65,0.72,0.61,0.55],
    'treatment_rev': [2.31,1.14,1.18,0.98,
                      0.89,0.84,0.79,0.88,0.71,0.61]
}
df = pd.DataFrame(data).sort_values('treatment_rev', 
                                     ascending=True)

fig, ax = plt.subplots(figsize=(9,5))
x = range(len(df))
ax.barh([i-0.2 for i in x], df['control_rev'], 
        height=0.4, label='Control ($39)', 
        color='#94a3b8')
ax.barh([i+0.2 for i in x], df['treatment_rev'], 
        height=0.4, label='Treatment ($59)', 
        color='#3b82f6')
ax.set_yticks(list(x))
ax.set_yticklabels(df['source'])
ax.set_xlabel('Avg Revenue Per User ($)')
ax.set_title('Revenue Per User by Acquisition Source')
ax.legend()
plt.tight_layout()

buf = io.BytesIO()
plt.savefig(buf, format='png', bbox_inches='tight')
buf.seek(0)
img_b64 = base64.b64encode(buf.read()).decode('utf-8')
img_b64
""",
  "mobile": """
import pandas as pd, matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
import io, base64

# Step 1: Compare mobile vs web revenue per user
data = {
    'metric': ['Revenue/User','Conversion Rate %'],
    'control_mobile': [0.81, 1.87],
    'treatment_mobile': [1.04, 1.62],
    'control_web': [0.73, 2.14],
    'treatment_web': [0.82, 1.48]
}
df = pd.DataFrame(data)

fig, axes = plt.subplots(1, 2, figsize=(10,4))
for i, row in df.iterrows():
    ax = axes[i]
    bars = ax.bar(['Mobile\\nControl','Mobile\\nTreatment',
                   'Web\\nControl','Web\\nTreatment'],
                  [row['control_mobile'],
                   row['treatment_mobile'],
                   row['control_web'],
                   row['treatment_web']],
                  color=['#94a3b8','#3b82f6',
                         '#94a3b8','#3b82f6'])
    ax.set_title(row['metric'])
    ax.set_ylabel(row['metric'])

fig.suptitle('Mobile vs Web Response to Price Increase', 
             fontsize=13, fontweight='bold')
plt.tight_layout()

buf = io.BytesIO()
plt.savefig(buf, format='png', bbox_inches='tight')
buf.seek(0)
img_b64 = base64.b64encode(buf.read()).decode('utf-8')
img_b64
"""
}

AGENT_CHECKLIST = {
    "sql_script": {
        "label": "SQL Agent",
        "checklist_items": [
            "Raw metrics fetched (CVR, Revenue, Sessions per variant)",
            "Both control and treatment variants have data",
            "No null/missing values in primary metric"
        ]
    },
    "srm_script": {
        "label": "SRM Check",
        "checklist_items": [
            "Traffic split is balanced — no Sample Ratio Mismatch",
            "No null session IDs in either variant",
            "Experiment date range matches intended run window"
        ]
    },
    "stats_script": {
        "label": "Statistician Agent",
        "checklist_items": [
            "Statistical significance calculated (Welch's t-test)",
            "CUPED variance reduction applied using pre-period covariate",
            "Pre-period covariate correlation validated (> 0.3)",
            "Observed effect vs minimum detectable effect validated"
        ]
    },
    "guardrail_script": {
        "label": "Guardrail Agent",
        "checklist_items": [
            "Error rate within acceptable threshold (< +0.25pp)",
            "Page load time within acceptable threshold (< +100ms)",
            "Cart abandonment rate not significantly worsened"
        ]
    },
    "rag_agent": {
        "label": "RAG / Context Agent",
        "checklist_items": [
            "Prior approved experiments searched for similar patterns",
            "Historical novelty effect risk assessed"
        ]
    },
    "post_analysis_agent": {
        "label": "Post-Analysis Agent",
        "checklist_items": [
            "Simpson's Paradox check run across all segments",
            "Segment breakdown generated (device, OS, source)"
        ]
    },
    "summary_agent": {
        "label": "Summary Agent",
        "checklist_items": [
            "Executive summary synthesized for non-technical audience",
            "Decision recommendation generated (LAUNCH / HOLD / INVESTIGATE)",
            "Confidence level assigned and justified"
        ]
    }
}
