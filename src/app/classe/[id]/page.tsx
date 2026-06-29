"use client";

import { useParams } from 'next/navigation';
import { coursPrimaire } from '../../../data/primaire';

export default function PageClasse() {
  const params = useParams();
  const id = params.id as string;

  // On cherche le cours correspondant à la classe (ex: CP)
  const cours = coursPrimaire.find((c) => c.id.startsWith(id));

  return (
    <main className="p-10 bg-gray-900 min-h-screen text-white">
      <h1 className="text-4xl font-bold mb-8">Classe de {id}</h1>
      
      {cours ? (
        <div className="bg-gray-800 p-8 rounded-2xl border border-gray-700 shadow-xl">
          <h2 className="text-3xl text-blue-400 mb-4">{cours.titre}</h2>
          <p className="text-gray-300 mb-6">{cours.description}</p>
          
          <div className="space-y-4">
            {cours.etapes.map((etape, index) => (
              <div key={index} className="p-4 bg-gray-700 rounded-lg">
                <span className="font-bold text-blue-300 uppercase text-sm">{etape.phase}</span>
                <p className="mt-1">{etape.contenu}</p>
              </div>
            ))}
          </div>
        </div>
      ) : (
        <p className="text-gray-400">Aucun cours disponible pour cette classe pour le moment.</p>
      )}
    </main>
  );
}