import React from 'react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Cell,
  ReferenceLine
} from 'recharts';
import { useProgressStore } from '../../stores/progressStore';
import { ModuleId } from '../../types/exam';

export const SubjectAccuracyChart: React.FC = () => {
  const { moduleStats } = useProgressStore();

  const moduleNames: Record<ModuleId, string> = {
    '1001': '1001 Mevzuat',
    '1003': '1003 Araçlar',
    '1005': '1005 Yatırım Kur.',
    '1012': '1012 Takas & Saklama',
  };

  const data = (Object.keys(moduleStats) as ModuleId[]).map((modId) => {
    const stat = moduleStats[modId];
    return {
      id: modId,
      name: moduleNames[modId],
      accuracy: stat.totalQuestions > 0 ? stat.averageAccuracy : 0,
      attempts: stat.attempts,
      total: stat.totalQuestions,
      bestScore: stat.bestScore,
    };
  });

  const getBarColor = (accuracy: number) => {
    if (accuracy >= 70) return '#059669'; // Emerald
    if (accuracy >= 50) return '#0D9488'; // Teal
    if (accuracy > 0) return '#D97706'; // Amber
    return '#E2E8F0'; // Muted Light Gray
  };

  return (
    <div className="w-full h-72 bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-5 space-y-3 shadow-sm">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-sm font-bold text-slate-900 dark:text-white tracking-wide">
            Modül Başarı Dağılımı (%)
          </h3>
          <p className="text-xs text-slate-500 dark:text-slate-400">
            Ders bazında ortalama doğru cevap oranı (SPK Barajı: %50)
          </p>
        </div>
        <div className="flex items-center gap-3 text-xs font-mono">
          <div className="flex items-center gap-1">
            <span className="w-2.5 h-2.5 rounded bg-emerald-600"></span>
            <span className="text-slate-700 dark:text-slate-300 font-semibold">≥ %70</span>
          </div>
          <div className="flex items-center gap-1">
            <span className="w-2.5 h-2.5 rounded bg-teal-600"></span>
            <span className="text-slate-700 dark:text-slate-300 font-semibold">%50 - %70</span>
          </div>
        </div>
      </div>

      <div className="w-full h-52">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
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
              tickFormatter={(v) => `${v}%`}
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
              formatter={(val: any) => [`%${val}`, 'Ortalama Başarı']}
              labelStyle={{ fontWeight: 'bold', color: '#0D9488' }}
            />
            <ReferenceLine y={50} stroke="#E11D48" strokeDasharray="3 3" label={{ value: 'SPK Barajı (%50)', fill: '#E11D48', fontSize: 10, position: 'insideTopRight' }} />
            <Bar dataKey="accuracy" radius={[8, 8, 0, 0]}>
              {data.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={getBarColor(entry.accuracy)} />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
