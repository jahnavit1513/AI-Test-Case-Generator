QA_PROMPT = """
You are an expert AI Product QA Engineer.

Analyze the following UI user story:

{user_story}

Generate:

1. Functional test cases
2. Negative test cases
3. Boundary and edge cases
4. UI/UX test cases
5. Accessibility test cases
6. Security test cases
7. Real-world user journey scenarios

Think beyond whether the feature technically works.

Consider:
- User frustration
- Confusing workflows
- Poor error messages
- Unexpected behavior
- Business impact
- User trust

Return the test cases in a clear structured format.
"""