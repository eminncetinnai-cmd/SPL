import React from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  ReferenceLine
} from 'recharts';
import { useProgressStore } from '../../stores/progressStore';

export const PerformanceTrendChart: React.FC = () => {
  const { history } = useProgressStore();

  // Last 10 quizzes in chronological order
  const data = [...history]
    .slice(0, 10)
    .reverse()
    .map((item, idx) => ({
      index: idx + 1,
      name: `Sınav ${idx + 1}`,
      title: item.title,
      score: item.score,
      accuracy: item.accuracy_pct,
      date: item.date,
    }));

  if (data.length === 0) {
    return (
      <div className="w-full h-72 bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-5 flex flex-col items-center justify-center text-center space-y-2 shadow-sm">
        <div className="p-3 rounded-full bg-slate-100 dark:bg-fintech-card text-slate-500 border border-slate-200 dark:border-fintech-border">
          📈
        </div>
        <h4 className="text-sm font-bold text-slate-800 dark:text-slate-300">Henüz Sınav Geçmişi Yok</h4>
        <p className="text-xs text-slate-500 max-w-xs">
          Test çözdükçe zaman içindeki başarı ve puan değişim grafiğiniz burada oluşacaktır.
        </p>
      </div>
    );
  }

  return (
    <div className="w-full h-72 bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-5 space-y-3 shadow-sm">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-sm font-bold text-slate-900 dark:text-white tracking-wide">
            Sınav Performans Trendi
          </h3>
          <p className="text-xs text-slate-500 dark:text-slate-400">
            Son 10 sınavdaki puan değişimi (SPK Geçme Barajı: 60 Puan)
          </p>
        </div>
        <div className="flex items-center gap-2 font-mono text-xs text-teal-700 dark:text-teal-400 font-bold">
          <span>Son Puan: {data[data.length - 1]?.score} / 100</span>
        </div>
      </div>

      <div className="w-full h-52">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#F1F5F9" vertical={false} />
            <XAxis 
              dataKey="name" 
              stroke="#64748B" 
              fontSize={11} 
              tickLine={false} 
              axisLine={{ stroke: '#E2E8F0' }} 
            />
            <YAxis 
              domain={[0, 100]} 
              stroke="#64748B" 
              fontSize={11} 
              tickLine={false} 
              axisLine={{ stroke: '#E2E8F0' }}
            />
            <Tooltip
              contentStyle={{
                backgroundColor: '#FFFFFF',
                borderColor: '#E2E8F0',
                borderRadius: '0.75rem',
                color: '#0F172A',
                fontSize: '12px',
                boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)',
              }}
              formatter={(val: any) => [`${val} Puan`, 'Sınav Skoru']}
              labelFormatter={(label, items) => {
                const item = items[0]?.payload;
                return item ? `${item.title} (${item.date})` : label;
              }}
            />
            <ReferenceLine y={60} stroke="#059669" strokeDasharray="3 3" label={{ value: 'Geçme Notu (60)', fill: '#059669', fontSize: 10, position: 'insideTopRight' }} />
            <Line
              type="monotone"
              dataKey="score"
              stroke="#0D9488"
              strokeWidth={3}
              dot={{ fill: '#0D9488', stroke: '#FFFFFF', strokeWidth: 2, r: 4 }}
              activeDot={{ r: 6, fill: '#0284C7' }}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
