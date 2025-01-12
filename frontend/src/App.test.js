import { render, screen } from '@testing-library/react';
import App from './App';

// Updated test to check if LoginPage renders correctly
test('renders LoginPage welcome message', () => {
  render(<App />);
  const welcomeElement = screen.getByText(/welcome to KS App/i);
  expect(welcomeElement).toBeInTheDocument();
});
