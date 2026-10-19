import React, { useMemo, useState } from 'react';
import { Award, BookOpen, GraduationCap, Search } from 'lucide-react';
import { LICENSE_CATALOG } from '../data/licenseCatalog';

interface LicensesPageProps {
  onNavigate: (page: string, params?: any) => void;
}

export const LicensesPage: React.FC<LicensesPageProps> = () => {
  const [search, setSearch] = useState('');
  const subjectLicenses = useMemo(() => {
    const licenses = new Map<string, string[]>();
    LICENSE_CATALOG.forEach((license) => {
      license.subjects.forEach((subject) => {
        licenses.set(subject, [...(licenses.get(subject) ?? []), license.name]);
      });
    });
    return licenses;
  }, []);

  const filtered = useMemo(() => {
    const query = search.trim().toLocaleLowerCase('tr-TR');
    if (!query) return LICENSE_CATALOG;
    return LICENSE_CATALOG.filter((license) =>
      `${license.name} ${license.education} ${license.subjects.join(' ')}`
        .toLocaleLowerCase('tr-TR')
        .includes(query)
    );
  }, [search]);

  return (
    <div className="space-y-6 animate-fade-in pb-16">
      <header className="rounded-3xl border border-teal-200 bg-gradient-to-br from-white via-teal-50 to-emerald-50 p-6 shadow-sm dark:border-teal-500/30 dark:from-fintech-surface dark:via-teal-950/30 dark:to-emerald-950/20 sm:p-8">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
          <div>
            <div className="mb-2 inline-flex items-center gap-2 rounded-full border border-teal-200 bg-teal-50 px-3 py-1 text-xs font-bold text-teal-800 dark:border-teal-500/30 dark:bg-teal-500/10 dark:text-teal-300">
              <Award className="h-4 w-4" />
              SPL Lisans Rehberi
            </div>
            <h1 className="text-2xl font-black tracking-tight text-slate-900 dark:text-white sm:text-3xl">
              Hangi lisans için hangi dersleri almalıyım?
            </h1>
            <p className="mt-2 max-w-3xl text-sm leading-relaxed text-slate-600 dark:text-slate-300">
              Her lisansın alması gereken dersleri ve bu derslerin hangi lisanslarla ortak olduğunu lisans bazında karşılaştırın.
            </p>
          </div>
          <div className="rounded-2xl border border-teal-200 bg-white/80 p-4 text-center dark:border-teal-500/20 dark:bg-fintech-card/70">
            <GraduationCap className="mx-auto mb-1 h-7 w-7 text-teal-600 dark:text-teal-400" />
            <div className="font-mono text-2xl font-black text-slate-900 dark:text-white">{LICENSE_CATALOG.length}</div>
            <div className="text-[11px] font-bold text-slate-500 dark:text-slate-400">Lisans türü</div>
          </div>
        </div>
        <div className="relative mt-6 max-w-xl">
          <Search className="absolute left-3 top-3 h-4 w-4 text-slate-400" />
          <input
            value={search}
            onChange={(event) => setSearch(event.target.value)}
            placeholder="Lisans veya ders ara..."
            className="w-full rounded-xl border border-slate-200 bg-white py-2.5 pl-10 pr-4 text-sm text-slate-900 outline-none focus:border-teal-500 dark:border-fintech-border dark:bg-fintech-card dark:text-white"
          />
        </div>
      </header>

      <div className="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm dark:border-fintech-border dark:bg-fintech-surface">
        <div className="overflow-x-auto">
          <table className="min-w-[980px] w-full border-collapse text-left text-sm">
            <thead className="bg-slate-100 text-xs uppercase tracking-wide text-slate-600 dark:bg-fintech-card dark:text-slate-300">
              <tr>
                <th className="w-[24%] border-b border-slate-200 p-4 dark:border-fintech-border">Lisans</th>
                <th className="w-[20%] border-b border-slate-200 p-4 dark:border-fintech-border">Eğitim şartı</th>
                <th className="border-b border-slate-200 p-4 dark:border-fintech-border">Dersler ve lisans ortaklığı</th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((license) => (
                <tr key={license.name} className="align-top transition-colors hover:bg-teal-50/40 dark:hover:bg-teal-500/5">
                  <td className="border-b border-slate-100 p-4 font-bold text-slate-900 dark:border-fintech-border/60 dark:text-white">
                    <div className="flex gap-2">
                      <BookOpen className="mt-0.5 h-4 w-4 shrink-0 text-teal-600 dark:text-teal-400" />
                      <span>{license.name}</span>
                    </div>
                    {license.note && (
                      <p className="mt-3 rounded-lg border border-amber-200 bg-amber-50 p-2 text-xs font-normal leading-relaxed text-amber-900 dark:border-amber-500/30 dark:bg-amber-950/30 dark:text-amber-200">
                        {license.note}
                      </p>
                    )}
                  </td>
                  <td className="border-b border-slate-100 p-4 text-slate-700 dark:border-fintech-border/60 dark:text-slate-300">
                    <span className="inline-flex rounded-lg bg-slate-100 px-2.5 py-1 text-xs font-bold text-slate-700 dark:bg-slate-800 dark:text-slate-200">
                      {license.education}
                    </span>
                  </td>
                  <td className="border-b border-slate-100 p-4 dark:border-fintech-border/60">
                    <ol className="grid gap-2 md:grid-cols-2">
                      {license.subjects.map((subject, index) => {
                        const sharedWith = subjectLicenses.get(subject) ?? [];
                        const sharedCount = sharedWith.length;
                        const badgeClass = sharedCount >= 4
                          ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-500/15 dark:text-emerald-300'
                          : sharedCount >= 2
                            ? 'bg-amber-100 text-amber-800 dark:bg-amber-500/15 dark:text-amber-300'
                            : 'bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300';
                        const otherLicenses = sharedWith
                          .filter((name) => name !== license.name)
                          .map((name) => name.replace('Sermaye Piyasası Faaliyetleri ', ''))
                          .join(', ');
                        return (
                        <li key={subject} className="rounded-lg border border-slate-100 bg-slate-50 px-3 py-2 text-xs leading-relaxed text-slate-700 dark:border-fintech-border/60 dark:bg-fintech-card/70 dark:text-slate-300">
                          <div className="flex gap-2">
                            <span className="font-mono font-bold text-teal-600 dark:text-teal-400">{index + 1}.</span>
                            <span className="font-semibold">{subject}</span>
                          </div>
                          <div className="mt-2 pl-5">
                            <span className={`inline-flex rounded-full px-2 py-1 text-[10px] font-black ${badgeClass}`}>
                              {sharedCount === 1 ? 'Bu lisansa özel' : `${sharedCount} lisansla ortak`}
                            </span>
                            {otherLicenses && (
                              <span className="ml-2 text-[10px] text-slate-500 dark:text-slate-400">
                                Ortak: {otherLicenses}
                              </span>
                            )}
                          </div>
                        </li>
                        );
                      })}
                    </ol>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        {filtered.length === 0 && (
          <div className="p-10 text-center text-sm text-slate-500 dark:text-slate-400">Aramanızla eşleşen lisans veya ders bulunamadı.</div>
        )}
      </div>
      <p className="text-xs leading-relaxed text-slate-500 dark:text-slate-400">
        Renkler: yeşil = 4+ lisansla ortak, amber = 2-3 lisansla ortak, gri = yalnızca bu lisansa özel. Sınav ve lisans koşulları değişebileceğinden başvuru öncesinde SPL’nin güncel resmi duyuruları kontrol edilmelidir.
      </p>
    </div>
  );
};
