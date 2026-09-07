// Blog Post Review Script

// Function to verify technical accuracy of the blog post
export function verifyBlogPost(steps, faq) {
  // Validate step-by-step walkthrough
  const stepsValid = steps.every(step => step.isValid());

  // Validate troubleshooting FAQ
  const faqValid = faq.every(entry => entry.isHelpful());

  return stepsValid && faqValid;
}