#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["pandas", "pyarrow", "requests"]
# ///
"""Test script to verify the jmail library works."""

import sys
sys.path.insert(0, "/home/ubuntu/jmail-client")

from jmail import JmailClient

# Test release_batches (small dataset)
print("Testing release_batches (smallest dataset)...")
client = JmailClient(cache=True)
df = client.release_batches()
print(df.to_string())

# Test people (also small)
print("\n\nTesting people dataset...")
people = client.people()
print(people[["name", "photo_count"]].to_string())

# Test the url helper
print("\n\nTesting url() helper...")
print(f"Emails slim URL: {client.url('emails-slim')}")
print(f"Emails slim NDJSON URL: {client.url('emails-slim', fmt='ndjson.gz')}")

# Test manifest
print("\n\nTesting manifest()...")
manifest = client.manifest()
print(f"Version: {manifest['version']}")
print(f"Datasets available: {list(manifest['datasets'].keys())}")

print("\n\nWoo! Yeah! All tests pass! What a ride!")