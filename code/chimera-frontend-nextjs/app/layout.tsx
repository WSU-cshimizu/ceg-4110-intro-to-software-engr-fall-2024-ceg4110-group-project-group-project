import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import ThemeProvider from "@/utils/ThemeProvider";
import NavigationBar from "@/components/NavigationBar/NavigationBar";
import Image from "../public/logo.png";
const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "Chimera",
  description: "Generated by create next app",
  icons: {
    icon: "logo-spp.jpg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="../public/logo.png" sizes="16*16"></link>
        <meta
          property="og:image"
          rel="icon"
          content="../public/logo.png"
        ></meta>
      </head>
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased bg-white dark:bg-gray-800`}
      >
        <ThemeProvider>
          <NavigationBar />
        </ThemeProvider>
        <div className="mt-5"></div>
        {children}
      </body>
    </html>
  );
}