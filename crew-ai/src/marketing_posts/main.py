#!/usr/bin/env python
import logging
import os
import sys
from typing import Any
from datetime import datetime

import yaml
from dotenv import load_dotenv

from marketing_posts.crew import MarketingPostsCrew

load_dotenv()
input_yaml = os.path.join(os.path.dirname(__file__), "config", "input.yaml")

logging.getLogger("LiteLLM").setLevel(logging.WARNING)


def parse_input() -> dict[str, Any]:
    with open(input_yaml) as f:
        inputs = yaml.safe_load(f)
    inputs['current_date'] = datetime.now().strftime("%Y-%m-%d")
    return inputs


def run() -> None:
    inputs = parse_input()
    MarketingPostsCrew().crew().kickoff(inputs=inputs)


def train() -> None:
    """
    Train the crew for a given number of iterations.
    """
    inputs = parse_input()
    try:
        MarketingPostsCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            filename="trained_agents_data.pkl",
            inputs=inputs,
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
