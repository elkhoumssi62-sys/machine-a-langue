import Link from 'next/link';

export default function Home() {
  const ecole = [
    { nom: "Primaire", classes: ["CP", "CE1", "CE2", "CM1", "CM2"] },
    { nom: "Collège", classes: ["6ème", "5ème", "4ème", "3ème", "Brevet"] },
    { nom: "Lycée", classes: ["T. Commun", "1ère BAC", "2ème BAC", "Prépa", "Culture"] }
  ];

  return (
    <main className="p-10 bg-gray-900 min-h-screen text-white">
      <h1 className="text-4xl font-bold mb-10 text-center">Bienvenue à la Machine à Langue</h1>
      
      {ecole.map((niveau) => (
        <section key={niveau.nom} className="mb-12">
          <h2 className="text-2xl font-semibold mb-6 border-b border-gray-700 pb-2">{niveau.nom}</h2>
          <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
            {niveau.classes.map((classe) => (
              <Link href={`/classe/${classe}`} key={classe}>
                <button className="p-6 bg-gray-800 border border-gray-700 rounded-xl hover:bg-blue-600 transition-all text-lg font-medium w-full">
                  {classe}
                </button>
              </Link>
            ))}
          </div>
        </section>
      ))}
    </main>
  );
}