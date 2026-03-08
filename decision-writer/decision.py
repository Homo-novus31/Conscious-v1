import json
from dataclasses import asdict
from datetime import datetime

def build_prompt(items, mode):
  system = """

You are an editorial strategist for an AI safety newsletter.

Your job is to examine the shortlisted research and decide the most important theme for this week's issue.

Explain briefly:
- what the central theme is
- why it matters right now
- which research items support it

Write a short editorial brief. Do NOT write the full article.Return only plain text
"""

  compressed_items = [
      {
          "title" : item['title'],
          "abstract" : item['abstract'][:500],
          "url" : item['url']
      }for item in items[:5]

  ]

  context = "Shortlisted Items:\n"


  for i, item in enumerate(compressed_items, 1):
    context += f"""
  Item {i}
  Title: {item['title']}
  Abstract: {item['abstract']}
  URL: {item['url']}
"""

  if mode == "train":
    instruction = """
    Mode: TRAIN
    Generate 2-3 DISTINCT DECISION SPECS.
    Each must represent a meaningfully different editorial decision.
    """
  elif mode == "infer":
    instruction = """
Mode: INFER

From the shortlisted items, produce a short editorial brief containing:

1. The main theme this week
2. Why it matters
3. Which research items support the theme

Keep it concise and analytical.Write plain text with all these specifications

  """
  else:
      # This case should ideally not be reached with current usage, but good to handle.
      instruction = ""
      print("Warning: Unknown mode for build_prompt.")

  # Combine system, context, and instruction. The schema is now part of the instruction.
  return f"System\n{system}\n{context}\n{instruction}"


def run_decision(items,mode):
  prompt = build_prompt(items,mode)
  output = generate_decision(prompt)
  if mode=="train":
    return output
  elif mode =="infer":
    return output


