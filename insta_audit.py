# ================= YOUR DETAILS =================
YOUR_NAME = "Samir"
YOUR_PHONE = "+91 6006372205"
YOUR_EMAIL = "samir147@gmail.com"
YOUR_TELEGRAM = "@Samir_18"
# ===============================================

from weasyprint import HTML


def safe_int(v, default=0):
    try:
        return int(v)
    except:
        return default


# ================= INPUT =================
print("\nInstagram Profile Audit Tool\n")

username = input("Instagram Username: ").strip()
followers = max(safe_int(input("Followers: ").strip()), 1)
likes = max(safe_int(input("Average Likes: ").strip()), 0)
comments = max(safe_int(input("Average Comments: ").strip()), 0)
posts_per_week = max(safe_int(input("Posts per week: ").strip()), 0)

raw_days = input("Analysis period (days) [7]: ").strip()
analysis_days = safe_int(raw_days) if raw_days else 7

raw_posts = input("Posts analyzed [5]: ").strip()
posts_analyzed = safe_int(raw_posts) if raw_posts else 5


# ================= FOLLOWER TIER =================
if followers < 500:
    tier = "Small"
elif followers < 5000:
    tier = "Medium"
else:
    tier = "Large"


# ================= STABILITY (FOR SCORE ONLY) =================
if followers < 100:
    stability = 0.6
elif followers < 500:
    stability = 0.8
elif followers < 1000:
    stability = 0.9
else:
    stability = 1.0


# ================= ENGAGEMENT =================
interaction_score = (likes * 0.7) + (comments * 1.5)
interaction_rate = (interaction_score / followers) * 100
normalized_engagement = interaction_rate * stability

final_score = min(int(normalized_engagement * 8), 100)


# ================= STATUS =================
if final_score >= 80:
    status = "Excellent"
elif final_score >= 60:
    status = "Good"
elif final_score >= 40:
    status = "Average"
else:
    status = "Poor"


# ================= TRAFFIC HELPERS =================
def traffic_label(level):
    return level  # "Strong" / "Average" / "Weak"


def traffic_status(value, green, orange):
    if value >= green:
        return "Strong"
    elif value >= orange:
        return "Average"
    else:
        return "Weak"


# ================= TIER-BASED THRESHOLDS =================
LIKE_THRESHOLDS = {
    "Small":  (0.06, 0.03),
    "Medium": (0.04, 0.02),
    "Large":  (0.025, 0.012)
}

COMMENT_THRESHOLDS = {
    "Small":  (0.010, 0.004),
    "Medium": (0.007, 0.003),
    "Large":  (0.004, 0.0015)
}


# ================= TRAFFIC CALCULATION =================
like_ratio = likes / followers
comment_ratio = comments / followers

# Engagement traffic (human sense cap)
if followers < 50:
    engagement_status = "Average"
elif interaction_rate >= 3:
    engagement_status = "Strong"
elif interaction_rate >= 1.5:
    engagement_status = "Average"
else:
    engagement_status = "Weak"

like_status = traffic_status(
    like_ratio,
    LIKE_THRESHOLDS[tier][0],
    LIKE_THRESHOLDS[tier][1]
)

comment_status = traffic_status(
    comment_ratio,
    COMMENT_THRESHOLDS[tier][0],
    COMMENT_THRESHOLDS[tier][1]
)

posting_status = (
    "Strong" if posts_per_week >= 5
    else "Average" if posts_per_week >= 3
    else "Weak"
)

stability_status = (
    "Strong" if stability >= 0.9
    else "Average" if stability >= 0.8
    else "Weak"
)


traffic_chart = {
    "Engagement Strength": engagement_status,
    "Like Activity": like_status,
    "Comment Interaction": comment_status,
    "Posting Consistency": posting_status,
    "Profile Stability": stability_status
}


# ================= MAIN OBSERVATION =================
weak_areas = [k for k, v in traffic_chart.items() if v == "Weak"][:3]

if not weak_areas:
    main_observation = (
        "Traffic analysis indicates balanced and stable performance across all key metrics. "
        "Engagement, interaction quality, and posting behavior are appropriate for the current account tier. "
        "No critical weaknesses were identified during the analyzed period. "
        "Content appears to resonate reasonably with the existing audience. "
        "Maintaining consistency and gradual improvement should support steady growth."
    )
else:
    main_observation = (
        "The analysis identifies weaknesses in the following areas: "
        + ", ".join(weak_areas) + ". "
        "These indicators suggest limited interaction depth or consistency relative to the account size. "
        "Weak performance in these areas can reduce organic reach and visibility. "
        "Such patterns often reflect gaps in content relevance or audience engagement triggers. "
        "Addressing these issues should be prioritized to improve overall profile performance."
    )


# ================= SUGGESTIONS =================
suggestions = [
    "Focus on creating content that delivers clear, repeatable value to the target audience.",
    "Improve the first few seconds of reels with stronger hooks and clearer visuals.",
    "Refine content themes and presentation if engagement remains inconsistent.",
    "Encourage discussion through opinion-based captions and direct calls-to-action.",
    "Maintain a consistent posting rhythm of three to five posts per week.",
    "Study high-performing posts to identify patterns worth repeating.",
    "Adopt a reel-first approach supported by concise storytelling.",
    "Create content that encourages saves and shares for long-term reach.",
    "Prioritize engaged followers over increasing follower count alone.",
    "Continuously adjust strategy based on performance insights."
]


# ================= HTML =================
html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{ font-family: Arial; background:#f1f3f6; padding:30px; }}
.header {{ background:#6a1b9a; color:white; padding:25px; border-radius:14px; }}
.card {{ background:white; padding:26px; border-radius:14px; margin-top:20px; }}
.problem {{ background:#fdecea; color:#c0392b; padding:22px; border-radius:14px; margin-top:20px; }}
.footer {{ background:#ede7f6; padding:20px; border-radius:12px; margin-top:30px; font-size:13px; }}
.green {{ color:#2ecc71; font-weight:bold; }}
.orange {{ color:#f39c12; font-weight:bold; }}
.red {{ color:#e74c3c; font-weight:bold; }}
</style>
</head>

<body>

<div class="header">
<h1>Instagram Profile Audit Report</h1>
<p><b>Prepared By:</b> {YOUR_NAME}</p>
<p>{YOUR_PHONE} | {YOUR_EMAIL} | {YOUR_TELEGRAM}</p>
</div>

<div class="card">
<p><b>Username:</b> {username}</p>
<p><b>Followers:</b> {followers}</p>
<p><b>Account Tier:</b> {tier}</p>
<p><b>Profile Score:</b> {final_score} / 100</p>
<p><b>Status:</b> {status}</p>
<p><b>Analysis Period:</b> Last {analysis_days} days</p>
<p><b>Posts Analyzed:</b> {posts_analyzed}</p>
</div>

<div class="card">
<h3>Traffic Light Performance Overview</h3>
<p>Engagement Strength: <span class="{ 'green' if engagement_status=='Strong' else 'orange' if engagement_status=='Average' else 'red' }">{engagement_status}</span></p>
<p>Like Activity: <span class="{ 'green' if like_status=='Strong' else 'orange' if like_status=='Average' else 'red' }">{like_status}</span></p>
<p>Comment Interaction: <span class="{ 'green' if comment_status=='Strong' else 'orange' if comment_status=='Average' else 'red' }">{comment_status}</span></p>
<p>Posting Consistency: <span class="{ 'green' if posting_status=='Strong' else 'orange' if posting_status=='Average' else 'red' }">{posting_status}</span></p>
<p>Profile Stability: <span class="{ 'green' if stability_status=='Strong' else 'orange' if stability_status=='Average' else 'red' }">{stability_status}</span></p>
</div>

<div class="problem">
<b>Main Observation</b><br><br>
{main_observation}
</div>

<div class="card">
<h3>Growth Recommendations</h3>
<ul>
""" + "".join(f"<li>{s}</li>" for s in suggestions) + """
</ul>
</div>

<div class="footer">
<b>Expert Note</b><br>
All observations are derived strictly from tier-based traffic indicators.<br>
This audit uses normalized engagement metrics and public activity signals only.<br>
The report is intended for strategic profile improvement purposes.
</div>

</body>
</html>
"""

HTML(string=html).write_pdf(f"{username}.pdf")
print("\nPDF generated successfully:", f"{username}.pdf")
