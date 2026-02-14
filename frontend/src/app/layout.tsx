import './globals.css';

export const metadata = {
  title: 'F&O Trading Intelligence Dashboard',
  description: 'Institutional-grade decision support for personal capital trading'
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
