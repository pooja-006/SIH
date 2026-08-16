export function translateReason(reason, t) {
  const skill = reason.match(/^Strong match because you know (.+)\.$/)
  if (skill) return t('reasons.skills', { skills: skill[1] })
  const interest = reason.match(/^Matches your interest in (.+)\.$/)
  if (interest) return t('reasons.interest', { sector: interest[1] })
  if (reason === 'Available in your preferred state.') return t('reasons.state')
  if (reason === 'Available in your preferred city.') return t('reasons.city')
  if (reason === 'Matches your preferred internship duration.') return t('reasons.duration')
  if (reason === 'Suitable based on your education profile and internship preferences.') return t('reasons.general')
  return reason
}
