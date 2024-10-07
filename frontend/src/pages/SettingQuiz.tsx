import * as React from "react"
import { MinusIcon, PlusIcon, ListBulletIcon, ActivityLogIcon } from "@radix-ui/react-icons"

import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer"
import { Label } from '@/components/ui/label';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Checkbox } from "@/components/ui/checkbox"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import {
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog"
import { Card } from "@/components/ui/card";
const SettingQuiz = () => {
  // const [timeLimit, setTimeLimit] = useState(60);
  // const [questionCount, setQuestionCount] = useState(10);
  // const [category, setCategory] = useState('general');


  // const handleStartQuiz = () => {
  //   onStartQuiz({ timeLimit, questionCount, category });
  // };

  return (
    <DialogContent className="sm:max-w-[425px]">
      <DialogHeader>
        <DialogTitle>Select vocabulary group</DialogTitle>
      </DialogHeader>
      <div className="max-h-60" style={{overflow: "auto"}}>
        <div className="p-2 shadow-inner" >
          {
            [1,2,3,4,5,6,7,8,9,10,11,22,33,42,34,23,42,34,23,4234,2,34,23,4,234,2,34,4,234,2,34,23,42,34,23,4,2].map((i:number)=>(
              <Card className="mb-4 p-2 flex justify-around"> 
                <Checkbox id="terms" className="mt-1" />
                <label
                  htmlFor="terms"
                  className="text-sm font-medium peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                >Vocabulary name</label>
                <div className="flex"><ActivityLogIcon className="mt-1 me-1"/> 5</div>
              </Card>
            ))
          }
        </div>    
      </div>
      <DialogFooter>
        <Button className="mt-1">Start Quiz</Button>
        <Drawer>
          <DrawerTrigger asChild>
            <Button variant={"outline"}>Change quiz params</Button>
          </DrawerTrigger>
          <QuizParams/>
        </Drawer>
      </DialogFooter>
    </DialogContent>
  );
};



const QuizParams = () => {
  return (
    <DrawerContent>
      <div className="mx-auto w-full max-w-sm p-3">
        <DrawerHeader>
          <DrawerTitle>Quiz Setup</DrawerTitle>
          <DrawerDescription>Set up your quiz settings</DrawerDescription>
        </DrawerHeader>
        <div className="space-y-2">
          <Label htmlFor="time-limit">Time Limit (seconds)</Label>
          <Input
            id="time-limit"
            type="number"
            // value={timeLimit}
            // onChange={(e) => setTimeLimit(Number(e.target.value))}
            min={30}
            max={300}
          />
        </div>
        <div className="space-y-2">
          <Label htmlFor="question-count">Number of Questions</Label>
          <Input
            id="question-count"
            type="number"
            // value={questionCount}
            // onChange={(e) => setQuestionCount(Number(e.target.value))}
            min={5}
            max={50}
          />
        </div>
        {/* <div className="space-y-2">
          <Label htmlFor="category">Category</Label>
          <Select
          // value={category} 
          // onValueChange={setCategory}
          >
            <SelectTrigger id="category">
              <SelectValue placeholder="Select a category" />
            </SelectTrigger>
            <SelectContent>
              {categories.map((cat) => (
                <SelectItem key={cat.value} value={cat.value}>
                  {cat.label}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div> */}
        <DrawerFooter>
          <Button>Ready</Button>
          <DrawerClose asChild>
            <Button variant="outline">Cancel</Button>
          </DrawerClose>
        </DrawerFooter>
      </div>
    </DrawerContent>
  )
}





export default SettingQuiz;
