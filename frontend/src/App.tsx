import * as React from "react"
import './App.css'

import QuizApp from '@/pages/Main'
import { ThemeProvider } from '@/components/theme-provider'


function App() {
  return (
    <ThemeProvider defaultTheme="light" storageKey="vite-ui-theme">
      <QuizApp />
    </ThemeProvider>
  )
}

export default App