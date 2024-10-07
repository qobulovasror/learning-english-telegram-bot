import { MixIcon, ListBulletIcon, TextAlignLeftIcon, PlusIcon } from "@radix-ui/react-icons"
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import {
  Dialog,
  DialogTrigger,
} from "@/components/ui/dialog"

import SettingQuiz from './pages/SettingQuiz';
import { ThemeProvider } from '@/components/theme-provider'


function App() {
  return (
    <ThemeProvider defaultTheme="light" storageKey="vite-ui-theme">
      <Card className="w-full max-w-sm mx-auto">
        <CardHeader>
          <CardTitle>Vocabulary booster</CardTitle>
        </CardHeader>
        <CardContent>
          <Dialog>
            <DialogTrigger asChild>
              <Button className='w-11/12 m-3 py-8 flex justify-around' variant="outline"><MixIcon /> Quiz <div></div></Button>
            </DialogTrigger>
            <SettingQuiz />
          </Dialog>
          <Button className='w-11/12 m-3 py-8 flex justify-around' variant={"outline"}><ListBulletIcon /> All words <div></div></Button>
          <Button className='w-11/12 m-3 py-8 flex justify-around' variant={"outline"}><TextAlignLeftIcon /> Own words <div></div></Button>
          <Button className='w-11/12 m-3 py-8 flex justify-around' variant={"outline"}><PlusIcon /> Add words <div></div></Button>
        </CardContent>
      </Card>
    </ThemeProvider>
  )
}

export default App



