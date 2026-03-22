import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "AlgoAlly - Premium AI DSA Companion",
  description: "Advanced AI-powered assistant for solving DSA problems.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark h-full antialiased">
      <body className={`${inter.className} h-full bg-[#020202] text-zinc-200 selection:bg-blue-500/20`}>
        {children}
      </body>
    </html>
  );
}
